import sys
import math
input = sys.stdin.readline
print = sys.stdout.write
while True:
    a = int(input())
    if a == 0:
        break
    print(str(math.comb(a+2,3))+'\n')
