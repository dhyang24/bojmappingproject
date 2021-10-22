n = int(input())
import math
def find(cur):
    global thing
    global visited
    global answer
    if visited[cur]: return 0
    visited[cur] = 1
    for i in range(len(thing[cur])):
        this = thing[cur][i]
        if answer[this] == -1 or find(answer[this]):
            answer[this] = cur
            return 1
    return 0
b = list(map(int,input().split()))
even = []
odd = []
for i in b:
    if i%2:
        odd.append(i)
    else:
        even.append(i)
thing = [[] for i in range(len(even)+1)]
for i in range(len(odd)):
    for p in range(len(even)):
        if math.gcd(odd[i],even[p]) != 1:
            continue
        anz = (odd[i]**2 + even[p]**2)
        lo = 0
        hi = 1414215
        stat = False
        while lo < hi:
            if hi-lo == 1:
                if hi**2 == anz or lo**2 == anz:
                    stat=True
                break
            mid = (lo+hi)//2
            if mid**2 == anz:
                stat = True
                break
            elif mid**2 < anz:
                lo = mid
            elif mid**2 > anz:
                hi = mid
        if stat:
            thing[p].append(i)
answer = [-1 for i in range(len(odd)+1)]
visited = [False for i in range(len(even)+1)]
ans = 0
for i in range(len(even)+1):
    visited = [False for i in range(len(even)+1)]
    if find(i):ans+=1
print(ans)
