for _ in range(int(input())):
    a = int(input())
    dic = {}
    for i in range(a):
        a, b, c = map(str, input().split())
        b, c = int(b), int(c)
        for i in range(b, c):
            try:
                dic[i] += 1
            except:
                dic[i] = 1
    dic = dict(sorted(dic.items()))
    for i in dic:
        print(chr(ord("A")+dic[i]-1), end='')
    print()