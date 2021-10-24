a = input()
ans = []
for _ in range(int(input())):
    b = input()
    stat = True
    for i in range(len(a)):
        if a[i] != "*" and a[i]!= b[i]:
            stat = False
            break
    if stat:
        ans.append(b)
print(len(ans))
print(*ans,sep='\n')