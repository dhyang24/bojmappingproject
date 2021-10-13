ga = 1
while True:
    zx = int(input())
    if zx == 0:
        break
    a = list(map(int,input().split()))
    avg = sum(a)//len(a)
    thing = 0
    for i in a:
        thing+=abs(avg-i)
    print("Set","#"+str(ga))
    print("The minimum number of moves is",str(thing//2)+'.')
    print()
    ga+=1