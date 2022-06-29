documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
}

def person_by_doc_num(file1):
  doc_num = input('Document number? ')
  for doc in file1:
    if doc_num in doc.values():
            print (f'Person with {doc_num} document number: {doc["name"]}')


def doc_in_shelf(file1):
    all_nums = list()
    for i in range (0, len(file1)):
        all_nums += list(file1.values())[i]
    doc_num = None
    while doc_num not in all_nums:
        doc_num = input(f'Which document? Choose from documents: {all_nums}  ')
        for k, v in file1.items():
            if doc_num in v:
                print (f'Document {doc_num} is in {k} shelf')


def all_docs(file1):
  for doc in file1:
        print (f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')

def add_new_doc(file1, file2):
  new_doc = dict()
  new_doc["type"] = input('Document type? ')
  new_doc["number"] = input('Document number? ')
  new_doc["name"] = input('Owner name? ')
  file1.append(new_doc)
  to_shelf = None
  while to_shelf not in file2.keys():
      to_shelf = input(f'Which directory? Choose from following shelves: {list(file2.keys())} ')
      if to_shelf in file2.keys():
          file2[to_shelf].append(new_doc["number"])
  print (file1)
  print (file2)

def delete_doc(file1, file2):
    all_nums = list()
    for i in range (0, len(file2)):
        all_nums += list(file2.values())[i]
    doc_num = None
    while doc_num not in all_nums:
        doc_num = input(f'Which document? Choose from documents: {all_nums}  ')
        for doc in file1:
            if doc_num in doc.values():
                file1.remove(doc)
        for k, v in file2.items():
            if doc_num in v:
                v.remove(doc_num)
    print (file1)
    print (file2)

def move_doc(file1):
    all_nums = list()
    for i in range (0, len(file1)):
        all_nums += list(file1.values())[i]
    doc_num = None
    to_shelf = None
    while doc_num not in all_nums:
        doc_num = input(f'Which document? Choose from documents: {all_nums}  ')
    while to_shelf not in file1.keys():
        to_shelf = input(f'To shelf? Choose from shelves {list(file1.keys())} ')
    moving_doc = None
    for v in file1.values():
        if doc_num in v:
            moving_doc = doc_num
            v.remove(doc_num)
    for k, v in file1.items():
        if to_shelf == k:
            v.append(moving_doc)
    print (file1)

def add_shelf(file1):
    trigger = 1
    while trigger:
        new_shelf = input(f'Create new shelf. Existing shelves: {list(file1.keys())} ')
        if new_shelf not in file1.keys():
            file1[new_shelf] = []
            trigger = 0
    print (file1)

def work_with_docs():
  while True:
    user_command = input('What do you want to do? Press q for exit ')
    if user_command == 'p':
      person_by_doc_num(documents)
    elif user_command == 's':
      doc_in_shelf(directories)
    elif user_command == 'l':
      all_docs(documents)
    elif user_command == 'a':
      add_new_doc(documents, directories)
    elif user_command == 'd':
      delete_doc(documents, directories)
    elif user_command == 'm':
      move_doc(directories)
    elif user_command == 'as':
      add_shelf(directories)
    elif user_command == 'q':
      print ('Bye!')
      break
work_with_docs()