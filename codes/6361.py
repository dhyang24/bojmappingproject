def thing(num):
    base = num[1]
    num = num[0]
    thing1 = [str(i) for i in range(10)] + [chr(ord('A')+j)
                                            for j in range(26)] + [chr(ord('a')+j) for j in range(26)]
    ans = ''
    if num == 0:
        return "0"
    while num > 0:
        ans += thing1[num % base]
        num = num//base
    return ans[::-1]


def thing2(num):
    base = num[1]
    num = list(num[0])
    thing1 = [str(i) for i in range(10)] + [chr(ord('A')+j)
                                            for j in range(26)] + [chr(ord('a')+j) for j in range(26)]
    ans = 0
    for i in range(len(num)):
        for p in range(len(thing1)):
            if thing1[p] == num[i]:
                ans += base**(len(num)-i-1)*p
    return ans


for _ in range(int(input())):
    q, w, e = map(str, input().split())
    print(q, e)
    e = thing2([e, int(q)])
    print(w, thing([e, int(w)]))
    print()
