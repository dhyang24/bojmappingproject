import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
pairs = int(input())
men = list(map(str, input().split()))
temp = {}
men2 = {}
for i in range(len(men)):
    temp[men[i]] = i
    men2[i] = men[i]
men = temp
women = list(map(str, input().split()))
temp = {}
women2 = {}
for i in range(len(women)):
    temp[women[i]] = i
    women2[i] = women[i]
women = temp
mens = {}
for i in range(pairs):
    temp = list(map(str, input().split()))
    temp2 = [men[temp[0]]]
    for p in range(1, len(temp)):
        temp2.append(women[temp[p]])
    ans = {}
    for p in range(1, len(temp)):
        ans[temp2[p]] = p
    mens[temp2[0]] = ans
womens = {}
for i in range(pairs):
    temp = list(map(str, input().split()))
    temp2 = [women[temp[0]]]
    for p in range(1, len(temp)):
        temp2.append(men[temp[p]])
    ans = {}
    for p in range(1, len(temp)):
        ans[temp2[p]] = p
    womens[temp2[0]] = ans
did = [[False for i in range(pairs)] for p in range(pairs)]
ans = [None for i in range(pairs)]
q = deque()
for i in range(pairs):
    q.append(i)
while q:
    now = q.popleft()
    for i in mens[now]:
        stat = False
        if not did[now][i]:
            if ans[i] == None:
                ans[i] = now
                stat = True
            else:
                if womens[i][ans[i]] > womens[i][now]:
                    stat = True
                    q.append(ans[i])
                    ans[i] = now
            did[now][i] = True
        if stat:
            break
for i in range(len(ans)):
    print(men2[ans[i]]+' '+women2[i]+'\n')
