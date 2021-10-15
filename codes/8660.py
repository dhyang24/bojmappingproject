a = int(input())
q, w = 0, 0
b = list(map(int, input().split()))
for i in b:
    if i < 0:
        q += 1
print(q*(a-1))
