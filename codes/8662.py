a = int(input())
b = list(map(int, input().split()))
ans = 0
temp = None
for i in range(len(b)-1, 0-1, -1):
    if temp == None:
        temp = b[i]
    else:
        if b[i] < temp:
            temp = b[i]
            continue
        else:
            ans += 1
            temp -= 1
            continue
if temp < 1:
    print(-1)
else:
    print(ans)
