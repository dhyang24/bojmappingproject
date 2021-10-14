for _ in range(int(input())):
    a = list(map(int, input().split()))
    a, b = a[0], a[1:]
    d = b[1]-b[0]
    stat = True
    for i in range(1, len(b)):
        if b[i]-b[i-1] != d:
            stat = False
            break
    if not stat:
        print("The sequence", str(b), "is not an arithmetic sequence.")
    else:
        print("The next 5 numbers after", str(b), "are:", str(
            [b[-1]+d, b[-1]+d*2, b[-1]+d*3, b[-1]+d*4, b[-1]+d*5]))
