import math
for _ in range(int(input())):
    a = input()
    if len(a) < 6:
        print(0)
        continue
    ans = math.inf
    for i in range(len(a)):
        for p in range(i,len(a)+1):
            if p-i > ans:
                continue
            stat = [False,False,False]
            for q in a[i:p]:
                if ord(q) >= ord('0') and ord(q) <= ord('9'):
                    stat[0] = True
                elif ord(q) >= ord('a') and ord(q) <= ord('z'):
                    stat[1] = True
                elif ord(q) >= ord('A') and ord(q) <= ord('Z'):
                    stat[2] = True
            if stat == [True,True,True]:
                ans = min(ans,p-i)
    print(max(6,ans) if ans != math.inf else 0)
