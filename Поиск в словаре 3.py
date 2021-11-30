def my_find(employer, name):
    for k, v in employer.items():
        if v['name'] == name:
            print(v['Telefon'])
            return

    print('Не найдено: "{}"'.format(name))


employer = {
    'id1': {
        'name': "Джон", 'Familia': "Трамп", 'Otchestvo': "Дональдович", 'Telefon': "33-33-33"
    },
    'id2': {
        'name': "Владимир", 'Familia': "Путин", 'Otchestvo': "Владимирович", 'Telefon': "8(912)911911911"
    }
}

name_id1 = input("Введите имя: ")

my_find(employer, name_id1)