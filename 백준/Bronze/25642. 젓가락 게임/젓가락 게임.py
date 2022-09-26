a,b = map(int,input().split())
while True:
    if a+b > 4:
        print("yt")
        break
    elif a+a+b > 4:
        print("yj")
        break
    a = a+a+b
    b = a+b
