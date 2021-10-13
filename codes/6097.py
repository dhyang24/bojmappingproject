a, b = map(int, input().split())
q = [1 for i in range(a)]
for i in range(b):
    w, e = map(int, input().split())
    for p in range(w-1, a, e):
        q[p] = 0
print(sum(q))
