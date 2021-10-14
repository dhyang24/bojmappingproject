while True:
    a = int(input())
    if a == 0:
        break
    b = list(map(int, input().split()))
    ans = 0
    for i in range(len(b)):
        ans += b[i]*(2**i)
    print(ans)
