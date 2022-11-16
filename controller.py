import csv_creator as cr
from export import print_data

def choice():
    print("Телефонная книга:\n\
    1 - Импорт;\n\
    2 - Печать;\n")
    ch = input("Введите цифру: ")
    if ch == '1':
        cr.writing_csv()
    elif ch == '2':
        print(print_data())
