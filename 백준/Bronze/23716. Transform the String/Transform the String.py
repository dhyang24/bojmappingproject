import math
for case in range(int(input())):
    q,w = input().strip(),input().strip()
    ans = 0
    for i in q:
        mn = math.inf
        for p in w:
            mn = min([mn,abs(ord(p)-ord(i)),26-abs(ord(p)-ord(i))])
        ans+=mn
    print("Case #"+str(case+1)+":",ans)

