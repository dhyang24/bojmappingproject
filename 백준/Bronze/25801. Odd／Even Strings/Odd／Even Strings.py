thing = [0 for i in range(26)]
a = (input())
for i in a:
    thing[ord(i)-ord('a')]+=1
stat = True
for i in thing:
    if i != 0 and i%2 == 0:
        stat = False
        break
if stat:
    print(1)
else:
    stat = True
    for i in thing:
        if i%2 != 0:
            stat = False
            break
    if stat:
        print(0)
    else:
        print("0/1")
        
