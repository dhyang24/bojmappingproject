a, b, c = map(int, input().split())
for p in range(b):
    q, w = map(int, input().split())
    print(abs(c-w)+q)
