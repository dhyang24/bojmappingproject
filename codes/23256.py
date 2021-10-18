import sys
input = sys.stdin.readline
print = sys.stdout.write
thing = [0 for i in range(1000001)]
b = 1
temp1 = 2
for i in range(1000001):
    thing[i] = b
    temp1 = ((temp1+b)*2)%1000000007
    b = (b + temp1)%1000000007
for _ in range(int(input())):
    a = int(input())
    print(str(thing[a]%1000000007)+'\n')
