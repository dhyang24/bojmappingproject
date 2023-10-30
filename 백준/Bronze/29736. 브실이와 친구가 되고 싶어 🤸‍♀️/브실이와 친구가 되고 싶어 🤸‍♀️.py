q,w=map(int,input().split())
e,r=map(int,input().split())
ans = 0
for i in range(q,w+1):
    if abs(i-e) <= r:
        ans+=1
print(ans if ans else "IMPOSSIBLE")
