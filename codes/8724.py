a = int(input())
b = list(map(int,input().split()))
ans = 0
temp = 0
for i in range(len(b)):
    if b[i] == 0:
        ans = max(temp,ans)
        temp = 0
    else:
        temp+=1
print(max(temp,ans))