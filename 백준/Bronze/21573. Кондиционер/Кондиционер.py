a,b = map(int,input().split())
c = input()
if c == 'heat':
    print(max(a,b))
elif c == 'freeze':
    print(min(a,b))
elif c == 'auto':
    print(b)
else:
    print(a)