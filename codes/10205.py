for qwer in range(int(input())):
    a = int(input())
    b = input()
    cur = a
    for i in b:
        if i == 'c':
            cur+=1
        else:
            cur-=1
    print("Data Set "+str(qwer+1)+':')
    print(cur)
    print()

