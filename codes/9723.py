for i in range(int(input())):
    a,b,c = sorted(map(int,input().split()))
    if a**2+b**2==c**2:
        print("Case #"+str(i+1)+':',"YES")
    else:
        print("Case #"+str(i+1)+':',"NO")