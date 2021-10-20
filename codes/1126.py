import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int,input().split()))
su = sum(b)
dp = [[-1 for i in range(su+1)] for i in range(len(b)+1)]
dp[0][0] = 0
thing = -1
for i in range(len(b)):
    for j in range(su+1):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        dp[i+1][j+b[i]] = max(dp[i][j]+b[i],dp[i+1][j+b[i]])
        if j < b[i]:
            dp[i+1][b[i]-j] = max(dp[i+1][b[i]-j],dp[i][j]+b[i]-j)
        elif j >= b[i]:
            dp[i+1][j-b[i]] = max(dp[i][j],dp[i+1][j-b[i]])
            if j-b[i] == 0:
                thing = max(dp[i][j],dp[i+1][j-b[i]])
print(thing)
