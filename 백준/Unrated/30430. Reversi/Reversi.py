ans = []
for i in range(int(input())):
    a,b = map(int,input().split())
    if a*b%4 == 0:
        ans.append("D")
    elif a*b%4 == 1:
        ans.append("W")
    elif a*b%4 == 2:
        ans.append("L")
    elif a*b%4 == 3:
        ans.append("L")
print(''.join(ans))