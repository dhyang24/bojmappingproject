from collections import deque
import sys
a = int(input())
b = [{} for i in range(a)]
c = [{} for i in range(a)]
for i in range(a):
    temp = list(map(int, input().split()))
    for p in range(a):
        temp[p] -= 1
    for p in range(a):
        b[i][temp[p]] = p
for i in range(a):
    temp = list(map(int, input().split()))
    for p in range(a):
        temp[p] -= 1
    for p in range(a):
        c[i][temp[p]] = p
did = [[False for i in range(a)] for p in range(a)]
ans = [None for i in range(a)]
q = deque()
for i in range(a):
    q.append(i)
while q:
    now = q.popleft()
    for i in c[now]:
        stat = False
        if not did[now][i]:
            if ans[i] == None:
                ans[i] = now
                stat = True
            else:
                if b[i][ans[i]] > b[i][now]:
                    stat = True
                    q.append(ans[i])
                    ans[i] = now
            did[now][i] = True
        if stat:
            break
for i in range(len(ans)):
    print(ans[i]+1)
