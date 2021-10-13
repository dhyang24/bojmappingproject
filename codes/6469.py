import math
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    stat = True
    for i in range(2, min(a, b)+1):
        if (not a % i) and (not b % i):
            stat = False
            break
    print(" "*(10-len(str(a)))+str(a)+" "*(10-len(str(b))) +
          str(b), "Good Choice" if stat else "Bad Choice")
    print()
