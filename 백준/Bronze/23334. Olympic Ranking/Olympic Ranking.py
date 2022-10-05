c = []
for i in range(int(input())):
    b = list(map(str,input().split()))
    c.append((int(b[0]),int(b[1]),int(b[2]),b[3:]))
print(*(max(c)[-1]),sep=' ')
