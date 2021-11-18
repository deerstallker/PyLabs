a = input("Верхний предел числового списка= ")

chisla = list(range(0, int(a)))

print(chisla)

result = []

for i in chisla:

    if ((i % 3) == 0 or (i % 5 == 0)):

        result.append(i)

print(result)

print("Сумма чисел меньше ",a ," ", "кратных 3 или 5 ","=" , sum(result))