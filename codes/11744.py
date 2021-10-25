import random
import sys
input = sys.stdin.readline
print = sys.stdout.write
qwer = int(input())
for i in range(500):
    temp = random.randint(0,2**(qwer)-1)
    ans = ''
    for p in range(qwer):
        if 2**p&temp:
            ans=ans+'1'
        else:
            ans=ans+'0'
    print(ans+'\n')
    sys.stdout.flush()
    thing = int(input())
    if thing != 0:
        break
if thing == qwer:
    pass
elif thing == 0:
    print("OH NO")
elif thing != qwer:
    tans = ""
    quad = False
    for i in range(qwer-2,-1,-1):
        ans = ""
        temp2 = temp^(2**(qwer-1))^(2**i)
        for q in range(qwer):
            if 2**q&temp2:
                ans=ans+'0'
            else:
                ans=ans+'1'
        print(ans+'\n')
        sys.stdout.flush()
        thing = int(input())
        if thing == qwer:
            quad = True
            break
        elif thing != qwer//2:
            tans=str("0" if (2**i&temp2) else "1")+tans
        else:
            tans=str("1" if (2**i&temp2) else "0")+tans
    if quad:
        pass
    else:
        ans = int(tans,2)*2+(temp//(2**(qwer-1)))
        tans3 = ''
        tans2 = ''
        for q in range(qwer):
            if 2**q&ans:
                tans3='1'+tans3
                tans2='0'+tans2
            else:
                tans3='0'+tans3
                tans2='1'+tans2
        print(tans3+'\n')
        sys.stdout.flush()
        thing = int(input())
        if thing != qwer:
            print(tans2+'\n')
            sys.stdout.flush()
