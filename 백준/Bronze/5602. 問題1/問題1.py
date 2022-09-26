a,b = map(int,input().split())
thing = [0 for i in range(b)]
for i in range(a):
    qwer = list(map(int,input().split()))
    for p in range(len(qwer)):
        thing[p]+=qwer[p]
z = [i+1 for i in range(b)]
z = sorted(z,key=lambda k:thing[k-1],reverse=True)
print(*z)
    
