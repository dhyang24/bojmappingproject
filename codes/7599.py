while True:
    a, b = map(str, input().split())
    if a == "#":
        break
    b = int(b)
    print(a, "Library")
    for i in range(1, int(input())+1):
        q, w = map(str, input().split())
        q = int(q)
        if len(w)*b + 2 > q:
            print("Book", i, "vertical")
        else:
            print("Book", i, "horizontal")
