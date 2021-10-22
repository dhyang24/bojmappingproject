import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
d = []
for i in range(int(input())):
    a = int(input())
    if a != 0:
        heapq.heappush(d,[abs(a),a])
    else:
        try:
            print(str(heapq.heappop(d)[1])+'\n')
        except:
            print(str(0)+'\n')
    
