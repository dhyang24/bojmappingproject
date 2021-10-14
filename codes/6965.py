for _ in range(int(input())):
    a = list(map(str, input().split()))
    for i in range(len(a)):
        if len(a[i]) == 4:
            a[i] = "****"
    print(*a)
    print()
