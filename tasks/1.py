
a, b, c = input().split()
 
if b > a < c:
    print(a)
elif a > b < c:
    print(b)
elif a > c < b:
    print(c)
 
if b < a > c:
    print(a)
elif a < b > c:
    print(b)
elif a < c > b:
    print(c)
