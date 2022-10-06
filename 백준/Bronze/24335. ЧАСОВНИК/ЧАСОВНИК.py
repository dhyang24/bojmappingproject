a,b,c,d,e = map(int,input().split())
a+=c
b+=d
a+=b//60
b = b%60
a = a%12
if e == 1:
    print(a,b)
else:
    if b%12 == 0:
        print("@",(a*5+b//12)%60)
    else:
        print((a*5+b//12)%60,(a*5+b//12+1)%60)
