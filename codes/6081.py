a, b = map(int, input().split())
data = []
for i in range(a):
    data.append(int(input()))
for i in range(b):
    q, w = map(int, input().split())
    ans = 0
    for p in range(q-1, w):
        ans += data[p]
    print(ans)
