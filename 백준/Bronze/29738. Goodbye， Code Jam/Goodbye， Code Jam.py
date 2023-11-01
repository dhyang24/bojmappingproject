for i in range(int(input())):
    q = int(input())
    print("Case #"+str(i+1)+":",end=' ')
    if q <= 25:
        print("World Finals")
    elif q <= 1000:
        print("Round 3")
    elif q <= 4500:
        print("Round 2")
    else:
        print("Round 1")