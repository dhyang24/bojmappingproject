a = int(input())
b = input()
ans = 0
for i in range(a//2):
    if b[i] != b[len(b)-1-i]:
        ans+=1
print(ans)
