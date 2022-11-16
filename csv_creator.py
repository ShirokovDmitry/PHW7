from ginfo import get_info

def writing_csv ():
    g = get_info()
    file = 'data.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {g[0]};Имя: {g[1]};Телефон: {g[2]}\n')