import pprint


# задача №1
def cook_dict(some_file: str):
    cook_book = dict()
    with open(some_file, 'r', encoding='utf-8') as book:
        for i in book:
            dish = i
            reagent_list = list()
            quantity = int(book.readline())
            for i in range(quantity):
                reagent_dict = dict()
                reagent = book.readline().strip().split('|')
                for i in range(len(reagent)):
                    reagent_dict['reagent'] = reagent[0]
                    reagent_dict['quantity'] = reagent[1]
                    reagent_dict['measure'] = reagent[2]
                reagent_list.append(reagent_dict)
            cook_book[dish.strip()] = reagent_list
            book.readline()
    return cook_book


#pprint.pprint(cook_dict('Cooking.txt'))


# задача №2
def total_reagents(dishes: list, persons: int):
    dish_dict = cook_dict('Cooking.txt')
    total = list()
    final = list()
    final_dict = dict()
    for i in dishes:
        for k, v in dish_dict.items():
            if k == i:
                for q in v:
                    q['quantity'] = int(q['quantity']) * persons
                    total.append(q)
    for i in list(total):
        if not i in final:
            final.append(i)
            total.remove(i)
    for i in final:
        for j in total:
            if i['reagent'] == j['reagent']:
                i['quantity'] = int(i['quantity']) + int(j['quantity'])
    for i in final:
        final_dict[i['reagent'].strip()] = {'measure': i['measure'], 'quantity': i['quantity']}
    return final_dict


#pprint.pprint(total_reagents(['Омлет', 'Фахитос'], 2))


# задача №3
len1 = 0
len2 = 0
len3 = 0
all_files_names = list()
all_len = list()
final = str()
with open('1.txt', 'r', encoding='utf-8') as file1:
    file_1 = file1.read().strip()
    file_1_name = file1.name
with open('1.txt', 'r', encoding='utf-8') as file1:
    for row in file1:
        len1 += 1
all_files_names.append({int(len1): [file_1_name, file_1]})
all_len.append(len1)


with open('2.txt', 'r', encoding='utf-8') as file2:
    file_2 = file2.read().strip()
    file_2_name = file2.name
with open('2.txt', 'r', encoding='utf-8') as file2:
    for row in file2:
        len2 += 1
all_files_names.append({int(len2): [file_2_name, file_2]})
all_len.append(len2)


with open('3.txt', 'r', encoding='utf-8') as file3:
    file_3 = file3.read().strip()
    file_3_name = file3.name
with open('3.txt', 'r', encoding='utf-8') as file3:
    for row in file3:
        len3 += 1
all_files_names.append({int(len3): [file_3_name, file_3]})
all_len.append(len3)
all_len = sorted(all_len)


for i in range(0, len(all_len)):
    for j in all_files_names:
        for k, v in j.items():
            if k == all_len[i]:
                final = final + v[0] + '\n' + str(k) + '\n' + v[1] + '\n'


with open('0.txt', 'a', encoding='utf-8') as file0:
    file0.write(final.strip())







