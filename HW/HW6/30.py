d = int(input("введите разность прогрессии "))
n = int(input("введите количевство элементов в прогрессии "))
a = [0]*n
a[0] = int(input("введите первый елемент прогрессии "))
prg = []
print(a[0], end = " ")
for i in range (1,n):
    a[i] = a[i-1]+d
    print(a[i], end=" ")

