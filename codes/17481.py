n,m = map(int,input().split())

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

thing = [[] for i in range(1001)]
thing1 = {}
thing2 = []
for i in range(m):
    thing1[input()] = i
for i in range(n):
    lis = list(map(str,input().split()))
    for q in range(1,len(lis)):
        thing[i].append(thing1[lis[q]])
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans = 0
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans+=1
if ans == n:
    print("YES")
else:
    print("NO")
    print(str(ans))
