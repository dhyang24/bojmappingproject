n,m,k1,k2 = map(int,input().split())

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
b = [[] for i in range(1001)]
thing = [[] for i in range(1001)]
for i in range(k1):
    lis = list(map(int,input().split()))
    thing[lis[0]-1].append(lis[1]-1)
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans = 0
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans+=1
b = [[] for i in range(1001)]
thing = [[] for i in range(1001)]
for i in range(k2):
    lis = list(map(int,input().split()))
    thing[lis[0]-1].append(lis[1]-1)
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans2 = 0
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans2+=1
print("그만 알아보자" if ans >= ans2 else "네 다음 힐딱이")
