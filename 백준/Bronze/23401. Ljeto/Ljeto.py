p1 = 0
p2 = 0
last = [-12341341234 for i in range(8)]
for i in range(int(input())):
    q,w,e = map(int,input().split())
    if last[w-1]+10 >= q:
        if w in [1,2,3,4]:
            p1+=150
        else:
            p2+=150
    else:
        if w in [1,2,3,4]:
            p1+=100
        else:
            p2+=100
    last[w-1] = q
print(p1,p2)
