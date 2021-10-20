import sys
import math
input = sys.stdin.readline
print = sys.stdout.write
a = int(input())
lis = list(map(int,input().split()))
numbers = list(set(lis))
tempthing = {}
for i in range(len(numbers)):
    tempthing[numbers[i]] = i
for i in range(len(lis)):
    lis[i] = tempthing[lis[i]]
numbers,tempthing = None,None
visited = [0 for i in range(10000001)]
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
            if visited[lis[i]] == 0:
                ans+=1
            visited[lis[i]] +=1
        current = [q,w]
        anss.append([qwery[p][2],ans])
    else:
        if q < current[0]:
            for i in range(q-1,current[0]-1):
                if visited[lis[i]] == 0:
                    ans+=1
                visited[lis[i]] +=1
        else:
            for i in range(current[0]-1,q-1):
                if visited[lis[i]] == 1:
                    ans-=1
                visited[lis[i]] -=1
        if w > current[1]:
            for i in range(current[1],w):
                if visited[lis[i]]  == 0:
                    ans+=1
                visited[lis[i]] +=1
        else:
            for i in range(w,current[1]):
                if visited[lis[i]]  == 1:
                    ans-=1
                visited[lis[i]] -=1
        current = [q,w]
        anss.append([qwery[p][2],ans])
anss.sort(key=lambda k:k[0])
for i in anss:
    print(str(i[1])+'\n')

        
