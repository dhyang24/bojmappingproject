x,y = map(int,input().split())
x = str(bin(x+(2**16)))[3:];y = str(bin(y+(2**16)))[3:]
ans = ""
for i in range(16):
    ans+=x[i]+y[i]
print(int(ans,2))
