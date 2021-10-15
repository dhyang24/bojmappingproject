while True:
    a = int(input())
    b = []
    if a == 0:
        break
    stat = True
    for i in range(a):
        q = list(map(str, input().split("-")))
        thing = [list(map(int, q[0].split(":"))),
                 list(map(int, q[1].split(":")))]
        thing = [thing[0][0]*60+thing[0][1], thing[1][0]*60+thing[1][1]]
        for i in b:
            if (i[0] < thing[0] and i[1] > thing[0]) or (i[0] < thing[1] and i[1] > thing[1]) or (i[0] < thing[0] and i[1] > thing[1]) or (i[0] > thing[0] and i[1] < thing[1]):
                stat = False
                break
        b.append(thing)
    print("no conflict" if stat else "conflict")
