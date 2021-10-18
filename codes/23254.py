import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
a,b = map(int,input().split())
a = a*24
lis = [[0 for i in range(2)] for i in range(b)]
inp = list(map(int,input().split()))
for i in range(b):
    lis[i][1] = inp[i]
inp = list(map(int,input().split()))
for i in range(b):
    lis[i][0] = inp[i]*-1
newlis = []
for i in lis:
    heapq.heappush(newlis,i)
ans = 0
while newlis:
    temp = heapq.heappop(newlis)
    temp[0] = temp[0]*-1
    mxtime = (100-temp[1])//temp[0]
    if a <= mxtime:
        ans+=temp[1]+(temp[0]*a)
        break
    a-=mxtime
    ans1 = mxtime*temp[0]+temp[1]
    if ans1 == 100:
        ans+=100
        continue
    else:
        heapq.heappush(newlis,[ans1-100,ans1])
while newlis:
    ans+=newlis.pop()[1]
print(str(ans)+'\n')
