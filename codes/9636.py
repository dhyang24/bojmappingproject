for i in range(int(input())):
    a = input()
    ans = [0,0]
    que = 0
    for i in range(len(a)):
        if a[i] =='?':
            que+=1
        elif a[i] == 'R':
            ans[0]+=1
        elif a[i] == 'L':
            ans[0]-=1
        elif a[i] == 'U':
            ans[1]+=1
        elif a[i] == 'D':
            ans[1]-=1
    print(ans[0]-que,ans[1]-que,ans[0]+que,ans[1]+que)