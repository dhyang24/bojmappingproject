import math
a = int(input())
c = 0
for i in range(a):
    q,w = map(int,input().split())
    c+=q*60+w
mn = math.inf
for i in range(1000):
    for j in range(1000):
        if i*240+j*180 >= c:
            mn = min(mn,i*1090+j*915)
print("{:.02f}".format(mn/100))
