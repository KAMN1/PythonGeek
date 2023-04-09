# Меньшее из двух
#Пользователь вводит два целых числа. Выведите меньшее из них.

print('A')
a = int(input())
print('B')
b = int(input())

if a<b:
    print(a)
elif b<a:
    print(b)
elif a == b:
    print("числа равны")    