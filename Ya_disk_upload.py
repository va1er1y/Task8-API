from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token:str):
        self.token = token

    def upload(self, file_path):
        name_file = file_path.split('\\')
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth { self.token}'}
   
        parameters = {"path":f'api_donl/second/ {name_file[-1]}', 'overwrite' : 'true'}
        res = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers = headers, params = parameters)
        if res.status_code == 200:
            href = res.json()['href']
            requests.put (href, data=open(file_path, 'rb'))
        else:
            print('Указан несуществующий путь на яндекс диске')

    def replace (self, path_start, path_end):
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth { self.token}'}
        parameters = {"from":path_start, "path" : path_end, 'overwrite' : 'true', 'force_async' :'true'}
        requests.post('https://cloud-api.yandex.net/v1/disk/resources/move', headers = headers, params = parameters)
        
if __name__ == '__main__':
  
  path_to_file = r'C:\Users\Валерий\Desktop\Запчасти.txt'
  token = ''
  uploader = YaUploader(token)
  result = uploader.upload(path_to_file)
  uploader.replace('api_donl/second', 'replaced')

  path_to_file2 = r'D:\Python\IMG_1007.jpg'
  uploader2 = YaUploader(token)
  uploader2.upload(path_to_file2)
