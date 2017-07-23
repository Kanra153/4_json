# Prettify JSON

Скрипт преобразует неструктурированный json в удобный для чтения вид.

# Как использовать

Пример запуска на Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

Пример результата:

{
   "firstName": "Иван",
   "lastName": "Иванов",
   "address": {
       "streetAddress": "Московское ш., 101, кв.101",
       "city": "Ленинград",
       "postalCode": 101101
   },
   "phoneNumbers": [
       "812 123-1234",
       "916 123-4567"
   ]
}

```


