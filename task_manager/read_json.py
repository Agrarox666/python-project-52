import json
from .settings import BASE_DIR


def get_json_data(filepath):
    with open(f'{BASE_DIR}/task_manager/fixtures/{filepath}', 'r') as json_file:
        data = json.load(json_file)
    return data
