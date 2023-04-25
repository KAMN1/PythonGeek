NM = [int(x) for x in input().split()]
n = NM[0]
m = NM[1]
set_1 = set()
set_2 = set()


a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)

b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i) 

lok = set_1 & set_2
result = list(lok)
result.sort()
print(result)
