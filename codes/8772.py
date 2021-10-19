for _ in range(int(input())):
    a = int(input())
    b = input()
    c = input()
    diff = ord(c)-ord(b[0])
    ans = []
    for i in b:
        ans.append(chr((ord(i)-ord('a')+diff)%26+ord('a')))
    print(*ans,sep='')
