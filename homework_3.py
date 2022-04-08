from csv import DictReader
import json

lst_books = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        lst_books.append(row)

with open("users.json", "r") as f:
    users = json.loads(f.read())

users_list = users[0:]
user_name = users_list[0]['name']

new_user_list = []
for i in range(len(users_list)):
    new_user_list.append({'name': users_list[i]['name'],
                          "gender": users_list[i]["gender"],
                          "address": users_list[i]["address"],
                          "age": users_list[i]["age"],
                          "books": []})

count = 0
for i in range(len(lst_books)):
    if count < len(new_user_list):
        new_user_list[count]["books"].append({'title': lst_books[i]['Title'], 'author': lst_books[i]['Author'],
                                              "pages": lst_books[i]['Pages'],
                                              "genre": lst_books[i]['Genre']})
        count += 1
    else:
        count = 0
        new_user_list[count]["books"].append(lst_books[i])

with open("example.json", "w") as f:
    s = json.dumps(new_user_list, indent=4)
    f.write(s)
