import json
import sys 

def load_data(filepath):
	with open(filepath, 'r') as raw_json:
		data = json.load(raw_json)
	return data	

def pretty_print_json(data):
	pprint = json.dumps(data, ensure_ascii=False, indent=3)
	return pprint


if __name__ == '__main__':
	filepath = sys.argv[1]
	data = load_data(filepath)
	pprint = pretty_print_json(data)
	print('Структурированный json:')
	print(pprint)
