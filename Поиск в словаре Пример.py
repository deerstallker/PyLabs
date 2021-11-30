
from pprint import pprint
import Levenshtein as ls
class Person:
    def __init__(self, height, name, age, hometown):
        self.height, self.name, self.age, self.hometown = height, name, age, hometown
        self.key = (height, name)
    def __repr__(self):
        return 'Person(%s, %s, %s, %s)' % (self.height, self.name, self.age, self.hometown)
maks = Person(197, 'Максим', 13, 'Пермь')
vlad = Person(188, 'Владимир', 49, 'Кемерово')
dmitr = Person(193, 'Дмитрий', 24, 'Свердловск')
anton = Person(202, 'Антоний', 33, 'Вятка')
people = {maks.key:maks, vlad.key:vlad, dmitr.key:dmitr, anton.key:anton}
pprint(people, sort_dicts = False)
field = input('По какому полю будем искать? ')
if field == 'рост':
    height = int(input('какого роста человека ищете? '))
    for key in people:
        if (key[0]>=height-2) and (key[0]<=height+2):
            print(people[key])
        else:
            print('ПОДХОДЯЩЕГО ЧЕЛОВЕКА НЕ НАЙДЕНО')
else:
    name = input('какого имени человека ищете? ')
    ind = False
    for key in people:
        if ls.distance(key[1].lower(), name.lower()) <= 2:
            print(people[key])
            ind = True
    if ind == False :
        print('ПОДХОДЯЩЕГО ЧЕЛОВЕКА НЕ НАЙДЕНО')