for case in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    ans = 0
    for i in range(1,len(b)-1):
        if b[i] > b[i+1] and b[i] > b[i-1]:
            ans+=1
    print("Case #"+str(case+1)+":",ans)
