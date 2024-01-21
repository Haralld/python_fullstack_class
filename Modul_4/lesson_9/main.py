import requests
import json


res = requests.get('http://numbersapi.com/05/09/date')
data = res.text

with open('date_info.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

