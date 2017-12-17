import json
import os


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        raw_json = json.load(file_handler)
    return raw_json


def pprint_json(raw_json):
    print(json.dumps(raw_json, ensure_ascii=False, indent=3))


if __name__ == '__main__':
    file_path = input('Введите путь до файла: ')
    if os.path.exists(file_path):
        raw_json = load_data(file_path)
        pprint_json(raw_json)
    else: 
        print('Файл не найден!')
