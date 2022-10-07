a = list(map(int,input().split()))
ans = []
for i in range(len(a)):
    if a[i] == 0:
        for p in range(1,5):
            if p not in a:
                ans.append((p,i))
                break
if len(ans) == 0:
    print(a[0],a[1])
elif len(ans) == 1:
    print(ans[0][1]+1,ans[0][0])
else:
    for i in range(1,5):
        if i not in a:
            print(i,end=' ')

