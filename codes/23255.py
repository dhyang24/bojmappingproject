import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write
a,b = map(int,input().split())
data = [[] for i in range(a)]
for i in range(b):
    q,w = sorted(map(int,input().split()))
    data[w-1].append(q-1)
    data[q-1].append(w-1)
tans = [0 for i in range(a)]
q = []
visited = [-1 for i in range(a)]
visited[0] = 0
visited2 = [-1 for i in range(a)]
for i in range(1,a):
    for q in data[i]:
        if visited[q] != -1:
            visited2[visited[q]] = True
    for q in range(a):
        if visited2[q] == -1: visited[i] = q;break
    for q in data[i]:
        if visited[q] != -1:
            visited2[visited[q]] = -1
for i in range(len(visited)):
    visited[i] = str(visited[i]+1)
print(" ".join(visited)+'\n')
        
    
