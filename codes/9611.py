c = [list(map(int,input().split()))for i in range(int(input()))]
for i in range(int(input())):
    a,b = map(int,input().split())
    a-=1
    ans = 0
    for p in range(len(c)):
        if p == a:
            continue
        if (abs(c[a][0]-c[p][0])**2 +abs(c[a][1]-c[p][1])**2) <= b**2:
            ans+=1
    print(ans)
