import sys
input = sys.stdin.readline
a,b = map(int,input().split())
c = list(map(int,input().split()))
ans = 0
for i in range(a-1):
    q = list(map(int,input().split()))
    t = 0
    for j in range(len(q)):
        t+=abs(q[j]-c[j])
    if t > 2000:
        ans+=1
if ans >= (a-1)/2:
    print("YES")
else:
    print("NO")