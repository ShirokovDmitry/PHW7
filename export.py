
def print_data():
    with open('data.csv', 'r', encoding='UTF-8') as file:
        file_read = file.read()
        print(file_read)