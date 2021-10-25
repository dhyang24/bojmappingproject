for qwer in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    c = [int(input()) for i in range(a)]
    for i in range(b):
        q,w,e,r = map(int,input().split())
        ans+=c[r-1]*q*w*e
    print("Data Set "+str(qwer+1)+":")
    print(ans)