while True:
    a = int(input())
    if not a:
        break
    mx = 0
    for i in range(1,1111):
        if i**3 > a**3:
            continue
        for j in range(1,1111):
            if i**3+j**3 > a**3:
                continue
            mx = max(mx,i**3+j**3)
    print(a**3-mx)
            
