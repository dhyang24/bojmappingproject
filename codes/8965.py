a = int(input())
for _ in range(a):
    b = input()
    c = b
    for i in range(len(b)):
        c= min(c,b[i:]+b[:i])
    print(c)