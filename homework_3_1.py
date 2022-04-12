import csv
import json
import os

if os.path.isfile('example.json'):
    os.remove('example.json')

with open("users.json", "r") as f:
    users = json.loads(f.read())

users_list_len = (i for i in users)
users_len = len(list(users_list_len))
users_list = (i for i in users)

with open('books.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    len_book = len(list(reader))

with open('books.csv', newline='') as f:
    reader = csv.reader(f)
    header1 = next(reader)
    book = (dict(zip(header1, row)) for row in reader)
    count_book = len_book % users_len
    count_user = 0
    with open("example.json", "a") as e:
        s1 = "[ \n"
        e.write(s1)
    for i in range(users_len):
        if count_user < count_book:
            one_user = next(users_list)
            one_user_short = {'name': one_user['name'],
                              "gender": one_user["gender"],
                              "address": one_user["address"],
                              "age": one_user["age"],
                              "books": []}

            for j in range((len_book // users_len) + 1):
                one_book = next(book)
                one_user_short["books"].append({'title': one_book['Title'], 'author': one_book['Author'],
                                                "pages": one_book['Pages'],
                                                "genre": one_book['Genre']})
            with open("example.json", "a") as e:
                s = json.dumps(one_user_short, indent=4)
                s1 = s + ", \n"
                e.write(s1)
            count_user += 1
        else:
            one_user = next(users_list)
            one_user_short = {'name': one_user['name'],
                              "gender": one_user["gender"],
                              "address": one_user["address"],
                              "age": one_user["age"],
                              "books": []}

            for j in range((len_book // users_len)):
                one_book = next(book)
                one_user_short["books"].append({'title': one_book['Title'], 'author': one_book['Author'],
                                                "pages": one_book['Pages'],
                                                "genre": one_book['Genre']})
            with open("example.json", "a") as e:
                s = json.dumps(one_user_short, indent=4)
                if count_user == users_len - 1:
                    s1 = s + "\n"
                else:
                    s1 = s + ", \n"
                e.write(s1)
            count_user += 1

    with open("example.json", "a") as e:
        s1 = "]"
        e.write(s1)
