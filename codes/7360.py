while True:
    a = int(input())
    if a == 0:
        break
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    p = [0,0]
    for i in range(a):
        if abs(b[i]-c[i]) > 1:
            if b[i] > c[i]:
                p[0]+=b[i]
            else:
                p[1]+=c[i]
        elif b[i] == c[i]:
            continue
        else:
            if b[i] > c[i]:
                p[1]+=(b[i]+c[i] if b[i] != 2 and c[i] != 1 else 6)
            else:
                p[0]+=(b[i]+c[i] if b[i] != 1 and c[i] != 2 else 6)
    print("A has",p[0],"points. B has",p[1],"points.",end='\n\n')