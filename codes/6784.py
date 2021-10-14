a = int(input())
data = [input() for i in range(a)]
ans = 0
for i in range(a):
    if data[i] == input():
        ans+=1
print(ans)