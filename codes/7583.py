while True:
    a = list(map(str, input().split()))
    if a[0] == "#":
        break
    for i in range(len(a)):
        if len(a[i]) == 1:
            continue
        a[i] = a[i][0]+a[i][1:-1][::-1]+a[i][-1]
    print(*a)
