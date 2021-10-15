import copy
import sys
input = sys.stdin.readline
q, w, e = map(int, input().split())
b = [[1 for i in range(w+1)] for i in range(q+1)]
for i in range(e):
    z, x = map(int, input().split())
    b[z-1][x-1] = 0
c = [[] for i in range(w+1)]
for i in range(q):
    for l in range(w):
        if b[i][l] == 1:
            c[l+1].append(i+1)
answer = [False for i in range(max(q, w)+1)]


def dfs(n):
    global c
    global visited
    global answer
    if visited[n]:
        return 0
    visited[n] = 1
    for i in range(len(c[n])):
        this = c[n][i]
        if not answer[this] or dfs(answer[this]):
            answer[this] = n
            return 1
    return 0


ans = 0
for i in range(len(c)):
    visited = [False for i in range(max(q, w)+1)]
    if dfs(i):
        ans += 1
print(ans)
