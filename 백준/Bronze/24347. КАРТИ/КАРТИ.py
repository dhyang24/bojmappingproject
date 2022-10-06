from itertools import permutations
a = list(map(str,input().split()))
mx = 0
for i in list(permutations(a,4)):
    mx = max(mx,int("".join(i)))
print(mx)
