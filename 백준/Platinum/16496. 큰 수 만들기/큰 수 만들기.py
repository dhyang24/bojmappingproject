def compare(a,b):
    return True if int(str(a)+str(b))>int(str(b)+str(a)) else False
a=int(input())
b = a
c = []
z = list(map(int,input().split()))
ans = ''
for i in range(a):
    temp = z[i]
    if len(c) ==0:
        c.append(temp)
    else:
        for p in range(len(c)+1):
            try:
                if compare(c[p],temp):
                    pass
                else:
                    c.insert(p,temp)
                    break
            except:
                c.insert(p,temp)
                break
stat = 0
for i in c:
    if i == max(c):
        if stat == 0:
            for l in range(b-a):
                ans+=str(i)
                stat = 1
    ans+=str(i)
print(int(ans))