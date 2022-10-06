a,b = map(int,input().split())
q,w,e = map(int,input().split())
for i in range((a+a-1)*(b)-1):
    q+=1
    if e%400 == 0 or (e%4 == 0 and e%100 != 0):
        if (q == 30 and w == 2) or (q == 31 and w not in [1,3,5,7,8,10,12]) or q == 32:
            q = 1
            w+=1
            if w == 13:
                w = 1
                e+=1
    else:
        if (q == 29 and w == 2) or (q == 31 and w not in [1,3,5,7,8,10,12]) or q == 32:
            q = 1
            w+=1
            if w == 13:
                w = 1
                e+=1
print(q,w,e)
