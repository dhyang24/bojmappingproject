import sys
input = sys.stdin.readline
print = sys.stdout.write
a = int(input())
for i in range(a):
    q,w,e = map(int,input().split())
    if (q+w*2+e*3)%2:
        print("No\n")
    else:
        if q == 0 and w%2 != 0:
            print("No\n")
        elif q>= e:
            print("Yes\n")
        else:
            print("No\n")