username = dict()

while True:
    name = input("Введите имя (или Enter - выход): ")
    if not name:
        break
    age = input("Введите возраст: ")
    isName = username.get(name, None)
    if isName is None:
        username[name] = age

print(username)
