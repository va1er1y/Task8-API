from pprint import pprint
from datetime import date, timedelta
import requests
import os

response = requests.get(f'https://api.stackexchange.com/2.3/questions?fromdate={(date.today() - timedelta(days=2))}&todate={date.today()}&order=asc&sort=activity&tagged=python&site=stackoverflow').json()
lens = len(response ['items'])
BASE_PATH = os.getcwd()
FILE_NAME = 'Stack_reference_log.txt'
text = os.path.join(BASE_PATH, FILE_NAME)
os.remove(text)
with open (text, 'a', encoding='utf-8') as file:
    for i in range (0,lens):
        file.write(str(response ['items'] [i] ['link']))
        file.write('\n')


