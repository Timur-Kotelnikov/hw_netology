import requests
import json


#задача 1
def smart_heroes(some_url, some_list):
    final = dict()
    data = json.loads(requests.get(some_url).text)
    for hero in data:
        if hero['name'] in some_list:
            final[hero['name']] = hero['powerstats']['intelligence']
    final = sorted(final.items(), key=lambda pair: pair[1], reverse=True)
    return f'Best of {some_list} is {final[0][0]} with {final[0][1]} intelligence!'


#print(smart_heroes('https://akabab.github.io/superhero-api/api/all.json', ['Hulk', 'Thanos', 'Captain America']))


#задача 2
class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                f'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        my_disk_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(my_disk_url, headers=headers)
        return response.json()

    def upload_link(self, some_path, name):
        headers = self.get_headers()
        params = {'path': some_path, 'overwrite': 'true'}
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2F'+name
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, some_path, name):
        href = self.upload_link(some_path=some_path, name=name)['href']
        response = requests.put(href, data=open(name, 'rb'))
        response.raise_for_status()

    def delete_file(self, name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': name}
        response = requests.delete(url=url, params=params, headers=self.get_headers())
        return response

    def show_trash(self):
        headers = self.get_headers()
        my_trash = 'https://cloud-api.yandex.net/v1/disk/trash/resources?path=%2F'
        response = requests.get(my_trash, headers=headers)
        return response.json()

    def clean_trash(self):
        headers = self.get_headers()
        my_trash = 'https://cloud-api.yandex.net/v1/disk/trash/resources?path=%2F'
        response = requests.delete(my_trash, headers=headers)
        return response

me = YandexDisk('token')
#me.upload_file(r'C:\Users\Пользователь\Desktop\it\python_hw', 'hw_1.py')
#me.delete_file('hw_1.py')
#me.clean_trash()
