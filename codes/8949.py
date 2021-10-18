a,b = sorted(map(int,input().split()))
a = str(a)
b = str(b)
ans = ''
for i in range(len(a)):
    ans = str(int(a[len(a)-1-i]) + int(b[len(b)-1-i]))+ans
print(b[:len(b)-len(a)]+ans)

