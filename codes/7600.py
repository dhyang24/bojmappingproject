while True:
    a = input().lower()
    if a == "#":
        break
    b = [0 for i in range(26)]
    for i in a:
        if ord(i) <= ord("z") and ord(i) >= ord("a"):
            b[ord(i)-ord('a')] = 1
    print(sum(b))
