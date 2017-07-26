import json
import sys
import os 

def load_data(filepath):
	if not os.path.exists(filepath):
		print('Вы ввели неправильный путь до файла')
		return None
	with open(filepath, 'r') as raw_json:
		data = json.load(raw_json)
	return data	

def pretty_print_json(data):
	pprint = json.dumps(data, ensure_ascii=False, indent=4)
	return pprint

if __name__ == '__main__':
	if len(sys.argv)>1:
			filepath = sys.argv[1]
			data = load_data(filepath)
			pprint = pretty_print_json(data)
			print('Структурированный json:')
			print(pprint)
	else: 
		print('Вы не ввели путь до файла')		
	 	
