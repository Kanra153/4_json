import json
import sys
import os 

def load_data(filepath):
    if not os.path.exists(filepath):
        print('Вы ввели неправильный путь до файла')
        exit()
    with open(filepath, 'r') as file_handler:
        raw_json = json.load(file_handler)
    return raw_json

def prettify_json(raw_json):
    pretty_json = json.dumps(raw_json, ensure_ascii=False, indent=3)
    return pretty_json

if __name__ == '__main__':
    if len(sys.argv)>1:
            filepath = sys.argv[1]
            raw_json = load_data(filepath)
            pprint = prettify_json(raw_json)
            print('Структурированный json: ', '\n', pprint)
    else: 
        print('Вы не ввели путь до файла')  
