a = input()
ans = []
key = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for i in range(len(a)//2):
    ans.append(int(a[i*2])*key[a[i*2+1]])
tans = 0
for i in range(1,len(ans)):
    if key[a[i*2+1]] <= key[a[(i-1)*2+1]]:
        tans+=ans[i-1]
    else:
        tans-=ans[i-1]
print(tans+ans[-1])