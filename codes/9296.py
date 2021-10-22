for qwer in range(int(input())):
    a = int(input())
    b = input()
    c = input()
    ans = 0
    for i in range(a):
        if b[i] != c[i]:
            ans+=1
    print("Case",str(qwer+1)+':',ans)