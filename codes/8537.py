mx = 0
for i in range(int(input())):
    c = {}
    for i in input():
        c[i] = 0
    mx = max(mx, len(c))
print(mx)
