dp = [0 for i in range(int(input())+1)]
for i in range(1,len(dp)):
    su = 0;
    for p in range(1,7):
        if (i-p >= 0):
            su+=dp[i-p]
    su = su*(1/6)
    dp[i]=su+1
print(dp[-1])
