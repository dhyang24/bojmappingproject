import sys
input = sys.stdin.readline
print = sys.stdout.write
a, b = map(int, input().split())
thing = []
for i in range(1, b+1):
    if b % i == 0:
        thing.append(i)
for i in range(1, a+1):
    if a % i == 0:
        for q in thing:
            print(str(i)+' '+str(q)+'\n')
