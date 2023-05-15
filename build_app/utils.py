import yaml


def load_yaml_file(filename):
    try:
        with open(filename) as f:
            return yaml.safe_load(f)
    except (FileNotFoundError, IOError) as e:
        raise ValueError(f'Error loading YAML file "{filename}": {str(e)}')


def create_dependency_dict(tasks):
    dependency_dict = {}
    for task in tasks:
        task_name = task['name']
        dependencies = set(task.get('dependencies', []))
        dependency_dict[task_name] = dependencies
    return dependency_dict


def find_build_by_name(builds, build_name):
    for build in builds:
        if build['name'] == build_name:
            return build
    return None


def sort_tasks(build, tasks):
    sorted_tasks = []
    visited = set()
    dependency_dict = create_dependency_dict(tasks)

    def visit(task_name):
        if task_name in visited:
            return
        visited.add(task_name)
        for dep_name in dependency_dict.get(task_name, []):
            visit(dep_name)
        sorted_tasks.append(task_name)

    for task_name in build['tasks']:
        visit(task_name)

    return sorted_tasks[::-1]


def get_sorted_tasks(build_name):
    tasks = load_yaml_file('builds/tasks.yaml')['tasks']
    builds = load_yaml_file('builds/builds.yaml')['builds']
    build = find_build_by_name(builds, build_name)
    if not build:
        raise ValueError(f'Build "{build_name}" not found')
    sorted_tasks = sort_tasks(build, tasks)
    return sorted_tasks
