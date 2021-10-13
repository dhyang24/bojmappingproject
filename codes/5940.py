a, b = map(int, input().split())
stat = False
for i in range(a+1, 63):
    if str(1 << i)[0] == str(b):
        print(i)
        stat = True
        break
if not stat:
    print(0)
