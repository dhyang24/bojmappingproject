import sys
import math
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
a,qwerqwer = map(int,input().split())
lis = list(map(int,input().split()))
visited = [deque() for i in range(100010)]
visited2 = [0 for i in range(100010)]
visited2[0] = 200000
current= None
ans = 0
qwery = []
anss = []
for i in range(int(input())):
    q,w = map(int,input().split())
    qwery.append([q,w,i])
qwery.sort(key=lambda k:k[0])
qwery.sort(key=lambda k:(k[1]//math.sqrt(a)))
for p in range(len(qwery)):
    q = qwery[p][0]
    w = qwery[p][1]
    if current == None:
        for i in range(q-1,w):
            stat = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
            visited2[stat]-=1
            visited[lis[i]].append(i)
            thing = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
            if ans < thing:
                ans = thing
            visited2[thing]+=1
        current = [q,w]
        anss.append([qwery[p][2],ans])
        
    else:
        if q < current[0]:
            for i in range(current[0]-2,q-2,-1):
                stat = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
                visited2[stat]-=1
                visited[lis[i]].appendleft(i)
                thing = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
                if ans < thing:
                    ans = thing
                visited2[thing]+=1
        if w > current[1]:
            for i in range(current[1],w):
                stat = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]]) != 0 else 0)
                visited2[stat]-=1
                visited[lis[i]].append(i)
                thing = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]]) != 0 else 0)
                if ans < thing:
                    ans = thing
                visited2[thing]+=1
        if not q < current[0]:
            for i in range(current[0]-1,q-1):
                stat = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
                visited2[stat]-=1
                visited[lis[i]].popleft()
                thing = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]])!= 0 else 0)
                visited2[thing]+=1
                if ans == stat and visited2[stat] == 0:
                    while visited2[ans] == 0:
                        ans-=1    
        
        if not w > current[1]:
            for i in range(current[1]-1,w-1,-1):
                stat = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]]) != 0 else 0)
                visited2[stat]-=1
                visited[lis[i]].pop()
                thing = (abs(visited[lis[i]][0]-visited[lis[i]][-1]) if len(visited[lis[i]]) != 0 else 0)
                visited2[thing]+=1
                if ans == stat and visited2[stat] == 0:
                    while visited2[ans] == 0:
                        ans-=1
        current = [q,w]
        anss.append([qwery[p][2],ans])
anss.sort(key=lambda k:k[0])
for i in anss:
    print(str(i[1])+'\n')