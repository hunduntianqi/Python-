import json
import csv

with open('app.js', 'r', encoding='utf-8') as file:
    dict_js = json.load(file)
    print(type(dict_js))
dict_list = []
tuple_headers = ('name', 'level1CategoryName', 'packageName')
dict_list.append(tuple_headers)
with open('./app.csv', 'w', encoding='utf-8') as file_w:
    write = csv.writer(file_w)
    for dict in dict_js:
        print(type(dict))
        dict_tuple = (dict['name'], dict['level1CategoryName'], dict['packageName'])
        dict_list.append(dict_tuple)
    write.writerows(dict_list)
