n,m,k = map(int,input().split())
b = [[] for i in range(1001)]
thing = [[] for i in range(1001)]
for i in range(n):
    lis = list(map(int,input().split()))
    for p in range(1,len(lis)):
        assert lis[p] <= m
        thing[i].append(lis[p]-1)
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
ans2 = 0
for i in range(n):
    if ans2 >= k:
        break
    visited = [False for i in range(1001)]
    if find(i):ans2+=1
print(ans+ans2)
