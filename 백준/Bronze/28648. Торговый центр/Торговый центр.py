a = int(input())
for i in range(a):
    q,w = map(int,input().split())
    try:
        ans = min(ans,q+w)
    except:
        ans = q+w
print(ans)
    