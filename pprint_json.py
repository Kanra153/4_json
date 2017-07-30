import json
import sys
import os 

def load_data(filepath):
    if not os.path.exists(filepath):
        print('Вы ввели неправильный путь до файла')
	return None
    with open(filepath, 'r') as file_handler:
        raw_json = json.load(file_handler)
    return raw_json

def pretty_print_json(raw_json):
    pprint = json.dumps(raw_json, ensure_ascii=False, indent=3)
    return pprint

if __name__ == '__main__':
    if len(sys.argv)>1:
            filepath = sys.argv[1]
            raw_json = load_data(filepath)
            pprint = pretty_print_json(raw_json)
            print('Структурированный json:')
            print(pprint)
    else: 
        print('Вы не ввели путь до файла')		
