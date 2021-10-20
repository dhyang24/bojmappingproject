a = input()
temp = a[0]
stat = False
for i in range(len(a)):
    if a[i] != temp:
        stat = True
        break
if not stat:
    print(-1)
else:
    if a == a[::-1]:
        print(len(a)-1)
    else:
        print(len(a))
