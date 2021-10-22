n,m = map(int,input().split())
b = [[] for i in range(1001)]
thing = [[] for i in range(1001)]
for i in range(m):
    lis = list(map(int,input().split()))
    thing[lis[0]-1].append(lis[1]-1)
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans = 0
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
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans+=1
print(ans)
