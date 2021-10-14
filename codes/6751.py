a = input()
for i in range(int(a)+1, 100000):
    stat = True
    q = [0 for i in range(10)]
    for p in str(i):
        q[int(p)] += 1
    for z in q:
        if z > 1:
            stat = False
            break
    if stat:
        print(i)
        break
