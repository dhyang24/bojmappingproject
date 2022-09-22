a = int(input())
mx = [-1,-1]
q = list(map(int,input().split()))
anss = []
for i in range(a):
    if q[i] >= max(mx):
        mx = [q[i],mx[0]]
    elif q[i] >= mx[1]:
        mx = [mx[0],q[i]]
    if mx[-1] != -1:
        anss.append(mx[-1])
print(*anss)

    
