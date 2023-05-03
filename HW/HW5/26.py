def calculat(A, B):
    if B == 1:
        return B
    if B != 1:
        return A * calculat(A,B-1)

A = int(input())
B = int(input()) + 1
print(calculat(A,B))
