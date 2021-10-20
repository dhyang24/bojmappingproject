import math
for i in range(int(input())):
    thing = str(bin(int(input())))[2:]
    ans = 0
    for i in range(len(thing)):
        if thing[i] == '1':
            ans = i
    print(0 if ans == 0 else ans+1)
