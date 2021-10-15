a, b, c, d = list(map(int, input().split())), list(map(int, input().split())), list(
    map(int, input().split())), list(map(int, input().split()))
a, b, c, d = sorted(
    sorted([a, b, c, d], key=lambda k: k[1]), key=lambda k: k[0])
if a[0] == b[0] and c[0] == d[0] and a[1] == c[1] and b[1] == d[1] and abs(b[1]-a[1]) == abs(c[0]-a[0]) and abs(c[0]-a[0]) != 0:
    print("TAK")
else:
    print("NIE")
