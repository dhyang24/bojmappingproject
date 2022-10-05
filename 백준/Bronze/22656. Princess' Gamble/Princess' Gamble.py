while True:
    a,b,c = map(int,input().split())
    if(a,b,c) == (0,0,0):
        break
    thing = []
    for i in range(a):
        thing.append(int(input()))
    total = sum(thing)*(100-c)
    print(0 if not thing[b-1] else total//thing[b-1])
    
