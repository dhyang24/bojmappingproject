for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mx = 0
    for i in range(a):
        for p in range(a):
            if p >= i and c[p] >= b[i]:
                mx = max(abs(i-p), mx)
    print("The maximum distance is", mx)
    print()
