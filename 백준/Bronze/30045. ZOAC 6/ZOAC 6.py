a = int(input())
ans = 0
for i in range(a):
    q = input()
    if "01" in q or "OI" in q:
        ans+=1
print(ans)