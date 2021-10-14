for _ in range(int(input())):
    a, b = map(str, input().split())
    b = int(b)
    c = a[len(a)-b:]+a[:-(b)]
    print("Shifting", a, "by", b, "positions gives us:", c)
