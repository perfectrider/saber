import yaml

def get_sorted_tasks(build_name):
    with open('builds/tasks.yaml', 'r') as f:
        tasks = yaml.safe_load(f)['tasks']

    with open('builds/builds.yaml', 'r') as f:
        builds = yaml.safe_load(f)['builds']

    build = None
    for b in builds:
        if b['name'] == build_name:
            build = b
            break
    if not build:
        raise ValueError(f'Build "{build_name}" not found')

    task_dict = {task['name']: task for task in tasks}

    dependency_dict = {}
    for task in tasks:
        for dependency in task.get('dependencies', []):
            if dependency not in dependency_dict:
                dependency_dict[dependency] = set()
            dependency_dict[dependency].add(task['name'])

    sorted_tasks = []
    visited = set()
    def visit(task_name):
        if task_name in visited:
            return
        visited.add(task_name)
        task = task_dict[task_name]
        for dependency_name in task.get('dependencies', []):
            visit(dependency_name)
        sorted_tasks.append(task_name)

    for task_name in build['tasks']:
        visit(task_name)

    return sorted_tasks[::-1]

