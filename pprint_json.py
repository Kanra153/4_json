import json
import os
import sys


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        parsed_json = json.load(file_handler)
    return parsed_json


def pprint_json(parsed_json):
    print(json.dumps(parsed_json, ensure_ascii=False, indent=3))


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        parsed_json = load_data(file_path)
        pprint_json(parsed_json)
    else:
        print('Файл не найден!')
