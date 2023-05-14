import yaml


def get_sorted_tasks(build_name):
    with open('builds/tasks.yaml') as f:
        tasks = yaml.safe_load(f)['tasks']
    with open('builds/builds.yaml') as f:
        builds = yaml.safe_load(f)['builds']

    build = next((b for b in builds if b['name'] == build_name), None)
    if not build:
        raise ValueError(f'Build "{build_name}" not found')

    dependency_dict = {
        t['name']: set(d for d in t.get('dependencies', [])) for t in tasks
    }

    sorted_tasks = []
    visited = set()

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


