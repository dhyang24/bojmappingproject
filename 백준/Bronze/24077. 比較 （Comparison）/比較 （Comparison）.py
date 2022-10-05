a,b = map(int,input().split())
c = list(map(int,input().split()))
d = list(map(int,input().split()))
ans = 0
for i in c:
    for j in d:
        if i<=j:
            ans+=1
print(ans)
