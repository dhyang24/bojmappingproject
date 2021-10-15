import sys
input = sys.stdin.readline
print = sys.stdout.write
a = int(input())
c = 0
mx = 0
for i in map(int, input().split()):
    mx = max(mx, c-i)
    c = max(i, c)
print(str(mx)+'\n')
