n,m = map(int,input().split())
thing = [[] for i in range(n)]
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
for i in range(m):
    lis = list(map(int,input().split()))
    if lis[0]%2 == lis[1]%2:
        continue
    if lis[0]%2 == 0:
        thing[lis[0]//2].append(lis[1]//2)
    else:
        thing[lis[1]//2].append(lis[0]//2)
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans = 0
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans+=1
print(ans*2+1 if ans*2 != n else ans*2)