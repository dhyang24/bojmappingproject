for i in range(int(input())):
    a,b = map(str,input().split())
    stat = True
    for q in b:
        if q not in a:
            stat = False
            break
    for q in a:
        if q not in b:
            stat=False
            break
        
    print("YES"if stat else 'NO')