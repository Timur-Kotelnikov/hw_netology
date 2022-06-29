import requests
import time
import json

yandex_token = 'token'
vk_token = 'token'


def get_foto_dict(person_id):
    url = 'https://api.vk.com/method/photos.get'
    params = {'owner_id': person_id, 'album_id': 'profile','extended': '1', 'access_token': vk_token, 'v': '5.131'}
    profile_fotos = requests.get(url=url, params=params).json()['response']['items']
    profile_fotos_dict = dict()
    profile_fotos_likes = list()
    for foto in profile_fotos:
        profile_fotos_likes.append(foto['likes']['count'])
    for foto in profile_fotos:
        max_size = 0
        for foto_copies in foto['sizes']:
            if foto_copies['width'] > max_size:
                max_size = foto_copies['width']
                foto_url = foto_copies['url']
                foto_size = f"{foto_copies['width']}*{foto_copies['height']}"
        if profile_fotos_likes.count(foto['likes']['count']) > 1:
            profile_fotos_dict[str(foto['likes']['count']) + ' likes' + ' Date = ' + time.ctime(foto['date']).replace(':', '-') + '.jpg'] = foto_url
        else:
            profile_fotos_dict[str(foto['likes']['count']) + ' likes.jpg'] = foto_url
    return profile_fotos_dict


def get_foto_list(person_id):
    url = 'https://api.vk.com/method/photos.get'
    params = {'owner_id': person_id, 'album_id': 'profile', 'extended': '1', 'access_token': vk_token, 'v': '5.131'}
    profile_fotos = requests.get(url=url, params=params).json()['response']['items']
    profile_fotos_likes = list()
    final_list = list()
    for foto in profile_fotos:
        profile_fotos_likes.append(foto['likes']['count'])
    for foto in profile_fotos:
        max_size = 0
        for foto_copies in foto['sizes']:
            if foto_copies['width'] > max_size:
                max_size = foto_copies['width']
                foto_size = f"{foto_copies['width']}*{foto_copies['height']}"
        if profile_fotos_likes.count(foto['likes']['count']) > 1:
            final_list.append({'file_name': (str(foto['likes']['count']) + ' likes' + ' Date = ' + time.ctime(foto['date']).replace(':', '-') + '.jpg'), 'size': foto_size})
        else:
            final_list.append({'file_name': (str(foto['likes']['count']) + ' likes.jpg'), 'size': foto_size})
    return final_list


def make_it_json(user_id, some_data):
    with open(f'{user_id}.json', 'w') as f:
        json.dump(some_data, f, ensure_ascii=False)


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', f'Authorization': f'OAuth {self.token}'}

    def new_folder(self, folder_name):
        params = {'path': folder_name}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.get_headers(), params=params)
        return response.json()

    def upload_foto(self, some_name, some_url):
        params = {'url': some_url, 'path': some_name}
        response = requests.post(url='https://cloud-api.yandex.net/v1/disk/resources/upload', params=params, headers=self.get_headers())
        response.raise_for_status()

    def upload_all_fotos(self, some_dict, user_id=None):
        count = 0
        for k, v in some_dict.items():
            count += 1
            self.upload_foto(some_name=f'/{user_id}/{k}', some_url=v)
            print(f'Foto {k} is in cloud! Progress = {count}/{len(some_dict)}')

    def all_in_one(self, user_id):
        self.new_folder(user_id)
        self.upload_all_fotos(get_foto_dict(user_id), user_id)
        make_it_json(user_id, get_foto_list(user_id))


me = YandexDisk(yandex_token)
me.all_in_one(user_id=)

