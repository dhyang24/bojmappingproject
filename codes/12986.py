import sys
import math
input = sys.stdin.readline
print = sys.stdout.write
a,qwerqwer = map(int,input().split())
lis = list(map(int, input().split()))
for i in range(len(lis)):
    lis[i]+=100000
visited = [0 for i in range(200002)]
visited2 = [0 for i in range(200002)]
visited2[0] = 2000002
current = None
ans = 0
qwery = []
anss = []
for i in range(qwerqwer):
    q, w = map(int, input().split())
    qwery.append([q, w, i])
qwery.sort(key=lambda k: k[0])
qwery.sort(key=lambda k: (k[1]//math.sqrt(a)))
for p in range(len(qwery)):
    q = qwery[p][0]
    w = qwery[p][1]
    if current == None:
        for i in range(q-1, w):
            visited2[visited[lis[i]]] -= 1
            if ans == visited[lis[i]]:
                ans += 1
            visited2[visited[lis[i]]+1] += 1
            visited[lis[i]] += 1
        current = [q, w]
        anss.append([qwery[p][2], ans])
    else:
        if q < current[0]:
            for i in range(q-1, current[0]-1):
                visited2[visited[lis[i]]] -= 1
                if ans == visited[lis[i]]:
                    ans += 1
                visited2[visited[lis[i]]+1] += 1
                visited[lis[i]] += 1
        else:
            for i in range(current[0]-1, q-1):
                visited2[visited[lis[i]]] -= 1
                if ans == visited[lis[i]] and visited2[visited[lis[i]]] == 0:
                    ans -= 1
                visited2[visited[lis[i]]-1] += 1
                visited[lis[i]] -= 1
        if w > current[1]:
            for i in range(current[1], w):
                visited2[visited[lis[i]]] -= 1
                if ans == visited[lis[i]]:
                    ans += 1
                visited2[visited[lis[i]]+1] += 1
                visited[lis[i]] += 1
        else:
            for i in range(w, current[1]):
                visited2[visited[lis[i]]] -= 1
                if ans == visited[lis[i]] and visited2[visited[lis[i]]] == 0:
                    ans -= 1
                visited2[visited[lis[i]]-1] += 1
                visited[lis[i]] -= 1
        current = [q, w]
        anss.append([qwery[p][2], ans])
anss.sort(key=lambda k: k[0])
for i in anss:
    print(str(i[1])+'\n')
