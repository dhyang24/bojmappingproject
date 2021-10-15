while True:
    m = input()
    if m == "#":
        break
    dic = {}
    while True:
        try:
            a, b = map(str, input().split())
        except:
            break
        try:
            dic[a] += 1
            dic[a] -= 1
        except:
            dic[a] = 0
        if b == "L":
            dic[a] += 120
        elif b == "S":
            dic[a] += 150
        elif b == 'B':
            dic[a] += 150
        elif b == "N":
            dic[a] += 40
        elif b == "C":
            dic[a] += 160
        elif b == "D":
            dic[a] += 100
        elif b == "R":
            dic[a] += 100
        elif b == "O":
            dic[a] += 100
    ans = 0
    for i in dic:
        if dic[i] >= 200:
            ans += 1
    print(m, ans)
