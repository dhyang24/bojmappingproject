a,b=map(int,input().split())
ans = ""
x = 1
while len(ans)<=1000000:
    ans+=str(x)
    x*=a
print(ans[b-1])
