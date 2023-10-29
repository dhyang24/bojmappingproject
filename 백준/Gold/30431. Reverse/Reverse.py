import sys
a = int(input())
print(a)
print("A"*a)
b = input()
if b == "utopia":
    print(2,0,2)
    print(1,1)
    print(1,1)
    print(0)
else:
    print(2,0,1)
    print(1,1)
    print(0)
c = input()
if c == "swi":
    print("swi's cake is missing!")
    print(0)
    print(0)
else:
    print("swi's cake is missing!")
    print(1)
    print(c)
    print(0)
d = int(input())
if d == 0:
    print(1,1,1,1)
    print(1)
else:
    print(d,d,d,d)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                sys.stdout.write(" ".join(["0"]*d)+'\n')
e = int(input())
if e == 0:
    print(2)
    print(2,0)
    print(1,0)
else:
    print(e*2)
    for i in range(e*2):
        sys.stdout.write(str((i^1)+1)+' '+str(1)+'\n')
z = input()
print(len(z))
for f in z:
    if f == "W":
        print(1, 1)
    elif f == "D":
        print(2, 2)
    elif f == "L":
        print(1, 3)
