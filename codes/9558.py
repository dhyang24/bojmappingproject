for _ in range(int(input())):
    a = list(map(int,input().split()))[1:]
    b = list(map(int,input().split()))[1:]
    ans =3515231515314531
    for i in a:
        for p in b:
            ans = min(ans,abs(i-p))
    print(ans)