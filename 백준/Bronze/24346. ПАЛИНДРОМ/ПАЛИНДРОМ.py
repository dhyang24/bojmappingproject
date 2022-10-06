a = input()
b = [0 for i in range(100)]
for i in range(len(a)):
    b[ord(a[i])-ord('A')]+=1
ans = 0
for i in range(len(b)):
    if b[i]%2:
        ans+=1
print(1 if not ans else ans)
