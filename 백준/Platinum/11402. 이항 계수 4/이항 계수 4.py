import math
a,b,c = map(int,input().split())
a1 = []
b1 = []
ans = 1
if(b == 0 or b == a):
    print(1)
else:
    for i in range(math.ceil(math.log(a,c))):
        temp = a//(c**i)%c
        a1.append(temp)
    for i in range(math.ceil(math.log(b,c))):
        temp = b//(c**i)%c
        b1.append(temp)
    for i in range(max(len(a1),len(b1))):
        if i >= len(b1):
            ans=ans*math.comb(a1[i],0)%c
        else:
            if b1[i] > a1[i]:
                ans=0
                break
            ans=ans*math.comb(a1[i],b1[i])%c
    print(ans)
