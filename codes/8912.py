for _ in range(int(input())):
    b = int(input())
    c = list(map(int,input().split()))
    ans = 0
    for i in range(1,len(c)):
        for p in c[0:i]:
            if p <= c[i]:
                ans+=1
    print(ans)