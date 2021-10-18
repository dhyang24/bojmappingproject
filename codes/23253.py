import sys
input = sys.stdin.readline
print = sys.stdout.write
a,b = map(int,input().split())
stat = True
for i in range(b):
    q = int(input())
    p = list(map(int,input().split()))
    if p != sorted(p,reverse = True):
        stat = False
        break
if stat:
    print("Yes\n")
else:
    print("No\n")
