import sys
input = sys.stdin.readline
print = sys.stdout.write
a = int(input())
def find():
    global l1
    global l2
    global dp1
    global dp2
    global dp3
    dp1 = [c*2 for i in range(c)]
    dp2 = [c*2 for i in range(c)]
    dp3 = [c*2 for i in range(c)]
    if l1[0] + l2[0] <= d:
        dp1[0] = 1
        dp2[0] = 1
        dp3[0] = 1
    else:
        dp1[0] = 2
        dp2[0] = 1
        dp3[0] = 1
    for i in range(1,c):
        dp1[i] = dp1[i-1]+2
        dp2[i],dp3[i] = [dp1[i-1]+1]*2
        if l1[i] + l1[i-1] <= d:
            dp2[i] = min(dp2[i],dp3[i-1]+1)
        if l2[i] + l2[i-1] <= d:
            dp3[i] = min(dp3[i],dp2[i-1]+1)
        dp1[i] = min([dp1[i],dp2[i]+1,dp3[i]+1])
        if l1[i] + l2[i] <=d:
            dp1[i] = min(dp1[i], dp1[i-1]+1)
        if l1[i] + l1[i-1] <= d and l2[i] + l2[i-1] <= d:
            if i >= 2:
                dp1[i] = min(dp1[i],dp1[i-2]+2)
            else:
                dp1[i] = min(dp1[i],2)
for _ in range(a):
    c,d = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    mi = c*2
    dp1 = [c*2 for i in range(c)]
    dp2 = [c*2 for i in range(c)]
    dp3 = [c*2 for i in range(c)]  
    find()  
    ans = dp1[c-1]
    if c > 1:
        if l1[0] + l1[-1] <= d:
            temp = [l1[0],l1[-1]]
            l1[0] = d
            l1[-1] = d
            find()
            ans = min(ans,dp3[c-1])
            l1[0],l1[-1] = temp
        if l2[0] + l2[-1] <= d:
            temp = [l2[0],l2[-1]]
            l2[0] = d
            l2[-1] = d
            find()
            ans = min(ans,dp2[c-1])
            l2[0],l2[-1] = temp  
        if l1[0] + l1[-1] <= d and l2[0] + l2[-1] <= d:
            l1[0] = d
            l1[-1] = d
            l2[0] = d
            l2[-1] = d
            find()
            ans= min(ans,dp1[c-2])
    print(str(ans)+'\n')