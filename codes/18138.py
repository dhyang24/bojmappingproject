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
thing1 = []
thing2 = []
for i in range(n):
    thing1.append(int(input()))
for i in range(m):
    thing2.append(int(input()))
for i in range(len(thing1)):
    for p in range(len(thing2)):
        if (thing2[p]>=thing1[i]/2 and thing2[p]<=thing1[i]*3/4) or (thing2[p]>=thing1[i] and thing2[p]<=thing1[i]*5/4):
            thing[i].append(p)
answer = [-1 for i in range(1001)]
visited = [False for i in range(1001)]
ans = 0
for i in range(n):
    visited = [False for i in range(1001)]
    if find(i):ans+=1
print(ans)
