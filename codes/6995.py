for _ in range(int(input())):
    a = list(map(int, input().split()))
    b, c = [], []
    for i in range(len(a)//2):
        b.append(a[i*2])
        c.append(a[i*2+1])
    temp = []
    stat = True
    for i in range(len(c)-1):
        for p in range(i+1, len(c)):
            stat = abs(c[i]-c[p])
            if stat in temp:
                stat = False
                break
            temp.append(stat)
        if not stat:
            break
    print("Have a spread.          " if stat else "Do not have a spread.   ", end='')
    if sorted(b) == [0, 1, 2, 3, 4]:
        print("Have a rainbow.")
    else:
        print("Do not have a rainbow.")
