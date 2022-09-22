
while True:
    a,b = map(int,input().split())
    if(a,b) == (0,0):
        break
    c = []
    for i in range(b):
        c.append(list(map(int,input().split())))
    mx = 0
    for i in range(a):
        stat = 0
        for p in range(b):
            stat+=c[p][i]
        mx = max(stat,mx)
    print(mx)