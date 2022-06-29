#visits
import pprint


def geo_logs(some_list):
    for visit in list(some_list):
        for k, v in visit.items():
            if  'Россия' not in v:
                some_list.remove(visit)
    return some_list


geo_logs([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
    ])


#unique ids
def unique_ids(some_dict):
    list1 = list()
    for i in some_dict.values():
        list1 += i
    return list(set(list1))


unique_ids({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]})


# % of queries
def queries(some_list):
    max_words = 0
    for query in some_list:
        query = query.strip()
        if query.count(' ')+1 > max_words:
            max_words = query.count(' ')+1
    for i in range (1, max_words+1):
        same_len_query = 0
        for query in some_list:
            query = query.strip()
            if query.count(' ')+1 == i:
                same_len_query += 1
        if same_len_query > 0:
            return f"With {i} words {round(100*same_len_query/len(some_list))} % of queries"


queries([
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ])


#ads sales
def ads_sales(some_dict):
    sale_list = list()
    for sale in some_dict.values():
        sale_list.append(sale)
    max_sale = max(sale_list)
    for k, v in some_dict.items():
        if v == max_sale:
            return k


ads_sales({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98})

