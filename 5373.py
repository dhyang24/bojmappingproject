while True:
    a, b = map(int, input().split())
    if(a,b) == (0,0):break
    c = [0 for i in range(a)]
    for i in range(b):
        d = list(map(int, input().split()))
        for p in range(len(d)):
            c[p] += d[p]
    print("yes" if b in c else 'no')
