import sys
input = sys.stdin.readline
print = sys.stdout.write
a = "#"+"#".join(input().strip())+'#'
ans = 0
cur = 0
cur1 = 0
le = len(a)
ans = [0 for i in range(le)]
tans = 0
for i in range(le):
    if i<= cur:
        ans[i] = min(ans[cur1*2-i],cur-i)
    else:
        ans[i] = 0
    while (i-ans[i]-1 >= 0 and i+ans[i]+1<le and a[i-ans[i]-1] == a[i+ans[i]+1]):
        ans[i]+=1
    if cur < i + ans[i]:
        cur = i + ans[i]
        cur1 = i
    tans=max(ans[i],tans)
print(str(tans)+'\n')
