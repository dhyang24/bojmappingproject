import math
mod = 1000000000
a = int(input())
if a < 3:
    print(1)
else:
    trians = math.comb((a-2)*2,(a-2))//(a-1)
    print(trians%mod)
if a%2:
    print(0)
else:
    a = a//2
    quadans = math.comb((a-1)*3,(a-1))//((a-1)*2+1)
    print(quadans%mod)
