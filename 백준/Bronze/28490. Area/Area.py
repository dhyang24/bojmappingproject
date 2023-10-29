m=0
for i in range(int(input())):
    q,w=map(int,input().split())
    m=max(m,q*w)
print(m)