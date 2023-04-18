N = int(input())
X = int(input())
i = 1
Some_list = []
for _ in range(N):
    number = i
    Some_list.append(number)
    i = i+1
    
print(Some_list)
print(min(Some_list, key=lambda x: abs(x-X)))