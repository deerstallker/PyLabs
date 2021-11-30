employer = {'id1': {'name': "Олег", 'Familia': "Петров", 'Otchestvo': "Олегович", 'Phone': "8(919)1234567"},
            'id2': {'name': "Жорж", 'Phone': "8(912)1234567"},
            'id3': {'name': "Котя", 'Phone': "8(912)1234567"}}

name1 = input("Кого ищем?: ")
flag = True

for search_emploers in employer:
    if employer[search_emploers]['name'] == name1:
        print(employer[search_emploers]['Phone'])
        name1 = input("что то ещё?: ")
        flag = False

if flag:
   print('не знаю такого')
   name1 = input("Попробуй как то иначе: ")
   flag = True

   for search_emploers in employer:
       if employer[search_emploers]['name'] == name1:
           print(employer[search_emploers]['Phone'])
           name1 = input("что то ещё?: ")


   #while True:
       #s = input("набери уже чтонибудь")
       #print(s)