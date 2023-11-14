a,b = map(int,input().split())
c = sorted(map(int,input().split()),reverse = True)
start = 0
end = a
mxpos = 0
while start <= end:
    mid = (start+end)//2
    temp = b
    curh = 0
    for i in range(len(c)):
        if c[i] >= mid:
            curh+=1
        else:
            if c[i] == mid-1 and temp >= mid-c[i]:
                temp-=1
                curh+=1
    if curh >= mid:
        mxpos = max(mid,mxpos)
        start = mid+1
    else:
        end = mid-1
print(mxpos)
