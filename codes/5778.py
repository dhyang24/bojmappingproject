while True:
    a,b = map(int,input().split())
    if (a,b) == (0,0): break
    q = list(map(int,input().split()))
    w = [0 for i in range(a)]
    for i in q:
        w[i-1]+=1
    ans = 0
    for i in w:
        if i > 1:
            ans+=1
    print(ans)