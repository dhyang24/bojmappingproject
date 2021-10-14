for q in range(int(input())):
    b = int(input())
    c = list(map(str, input().split()))
    ans = 0
    for i in c:
        if i == 'sheep':
            ans += 1
    print("Case", str(q+1)+":", "This list contains",
          str(ans), "sheep.", end='\n\n')
