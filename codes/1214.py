import math
a,b,c = map(int,input().split())
b,c = sorted([b,c])
gcd = math.gcd(b,c)
mx = math.inf
if gcd*(b//gcd-1)*(c//gcd-1) <= a:
    print(gcd*math.ceil(a/gcd))
else:
    for i in range(math.ceil(a/c)+1):
        mx = min(mx,max(0,b*math.ceil((a-c*i)/b))+c*i)
    print(mx)