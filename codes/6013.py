a = int(input())
b = []
for i in range(a):
    b.append(list(map(int, input().split())))
thing = []
for i in range(len(b)-1):
    for p in range(i+1, len(b)):
        thing.append([abs(b[i][0]-b[p][0])**2 +
                     abs(b[i][1]-b[p][1])**2, i+1, p+1])
ans = max(thing, key=lambda k: k[0])
print(ans[1], ans[2])
