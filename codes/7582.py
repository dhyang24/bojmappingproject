while True:
    a, b = map(str, input().split())
    if (a, b) == ("#", "0"):
        break
    b = int(b)
    now = int(input())
    for i in range(int(input())):
        q, w = map(int, input().split())
        now = min(b, now-q+w)
    print(a, now)
