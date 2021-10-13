import copy
a = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    temp = copy.deepcopy(a)
    temp.remove(a[i])
    ans = 0
    for p in temp:
        if abs(a[i][0]-p[0])**2 + abs(a[i][1]-p[1])**2 <= (a[i][2]+p[2])**2:
            ans += 1
    print(ans)
