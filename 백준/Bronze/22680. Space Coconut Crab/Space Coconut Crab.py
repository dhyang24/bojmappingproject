import math
while True:
    a = int(input())
    if a == 0:
        break
    mn = math.inf
    for i in range(1001):
        for p in range(101):
            if i**2+p**3>a:
                continue
            mn = min(mn,i+p+(a-i**2-p**3))
    print(mn)
