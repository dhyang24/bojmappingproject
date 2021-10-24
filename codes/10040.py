a,b = map(int,input().split())
c = [int(input()) for i in range(a)]
ans = [0 for i in range(a)]
for i in range(b):
    q = int(input())
    for l in range(a):
        if c[l] <= q:
            ans[l]+=1
            break
for i in range(a):
    if ans[i] == max(ans):
        print(i+1)
        break