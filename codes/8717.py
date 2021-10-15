import math
a = int(input())
b = list(map(int, input().split()))
su = sum(b)
suz = 0
mn = math.inf
for i in range(len(b)-1):
    suz += b[i]
    mn = min(mn, abs(su-suz*2))
print(mn)
