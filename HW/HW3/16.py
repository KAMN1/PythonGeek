N = int(input())
X = int(input())
x = 0
Some_list = []
for _ in range(N+1):
    number = x
    Some_list.append(number)
    x = x+1
    
print(Some_list)
print(Some_list.count(X))
