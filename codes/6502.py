stat = 1
while True:
    a = input()
    if a == '0':
        break
    a, b, c = map(int, a.split())
    if (b**2+c**2 <= (a*2)**2):
        print("Pizza", stat, "fits on the table.")
    else:
        print("Pizza", stat, "does not fit on the table.")
    stat += 1
