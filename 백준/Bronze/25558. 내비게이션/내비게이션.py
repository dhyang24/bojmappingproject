a = int(input())
b,c,d,e = map(int,input().split())
mn = [14351324141234123412412341241234,-1]
for i in range(a):
    cur = (b,c)
    ans = 0
    for p in range(int(input())):
        q,w = map(int,input().split())
        ans+=abs(cur[0]-q)+abs(cur[1]-w)
        cur = (q,w)
    q,w = d,e
    ans+=abs(cur[0]-q)+abs(cur[1]-w)
    mn = min(mn,(ans,i+1),key = lambda k:k[0])
print(mn[1])
