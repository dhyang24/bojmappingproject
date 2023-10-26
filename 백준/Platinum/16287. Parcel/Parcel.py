a,b = map(int,input().split())
c = list(map(int,input().split()))
d = [0,0,0,0]
for i in c:
    d[3] = d[3]|(d[2]<<i)
    d[2] = d[2]|(d[1]<<i)
    d[1] = d[1]|(d[0]<<i)
    d[0] = d[0]|(1<<i)
print("YES" if d[3]&(1<<a) else "NO")