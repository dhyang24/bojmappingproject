for _ in range(int(input())):
    print(sorted(sorted([list(map(int,input().split())) for i in range(int(input()))],key=lambda k:k[1]),key=lambda k:k[1]/k[0])[0][1])
