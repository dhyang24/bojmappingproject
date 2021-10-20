a = int(input())
for i in range(a):
    c = input()
    ans = 0
    thing = []
    cur = ''
    for i in range(len(c)):
        try:
            cur+=str(int(str(c[i])))
        except:
            thing.append(cur)
            thing.append(c[i])
            cur = ''
    thing.append(cur)
    for i in range(len(thing)):
        if thing[i] == 'C':
            try:
                ans+=12.01*int(thing[i+1])
            except:
                ans+=12.01
        elif thing[i] == 'H':
            try:
                ans+=1.008*int(thing[i+1])
            except:
                ans+=1.008
        elif thing[i] == 'O':
            try:
                ans+=16.00*int(thing[i+1])
            except:
                ans+=16.00
        elif thing[i] == 'N':
            try:
                ans+=14.01*int(thing[i+1])
            except:
                ans+=14.01
    print("{:.3f}".format(ans))




