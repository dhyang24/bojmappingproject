a,b,c,d,e,f,g = map(int,input().split())
mn = 123412341234124312341234
for i in range(d+1):
    for j in range(e+1):
        for l in range(f+1):
            if i*a+j*b+l*c >= g:
                mn = min(mn,i+j+l)
if mn == 123412341234124312341234:
    print(0)
else:
    print(mn)
                
