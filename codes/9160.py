import sys
input = sys.stdin.readline
a=[]
while True:
    try:
        q = input()
        for i in list(q):
            a.append(i.lower())
    except:
        break
thing = False
for i in range(len(a)):
    if a[i] == '.' or a[i] == '?' or a[i] == '!' or a[i] == "(" or a[i] == ')':
        thing = True
    else:
        if a[i] != ' ' and thing:
            a[i] = a[i].upper()
            thing = False
print(*a,sep='')
    