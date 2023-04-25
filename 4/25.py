text = input().split()
result = {}
print(text)
for i in text:
    if i in result:
        print(f'{i}_{result[i]}', end= " ")
        result[i] = result[i]+1
    else:
        print(i, end= " ")
        result[i] = 1