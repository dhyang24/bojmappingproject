b = int(input())
a = [0,1]
ans = [0 for i in range(b+1)]
ans[1] = 1
while True:
    a.append([a[-1],(a[-1]+a[-2])])
    ans[a[-1]] = a[-1]
    if a[-1] >= b:
        break
cur = 1
for i in range(b):
    if ans[i] != 0:
        cur = i
    else:
        ans[i] = ans[i-cur]

