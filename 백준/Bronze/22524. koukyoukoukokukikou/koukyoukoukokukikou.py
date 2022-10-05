a = "qwertasdfgzxcvb"
while True:
    z = input()
    if z == "#":
        break
    ans = 0
    for i in range(len(z)-1):
        if (z[i] in a) ^ (z[i+1] in a):
            ans+=1
    print(ans)
