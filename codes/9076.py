for i in range(int(input())):
    a = sorted(map(int,input().split()))
    print("KIN" if a[3]-a[1] >= 4 else sum(a[1:4]))