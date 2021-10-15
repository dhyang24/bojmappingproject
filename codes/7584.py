while True:
    a = list(map(str, input().split()))
    if a[0] == "#":
        break
    if len(a) == 10:
        print("Draw")
    elif len(a) % 2:
        print("O" if a[0] == "X" else "X")
    else:
        print(a[0])
