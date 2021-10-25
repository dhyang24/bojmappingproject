a = input()
for i in range(26):
    ans = ""
    for p in a:
        if ord(p) >= ord('A') and ord(p) <= ord('Z'):
            ans+=chr((ord(p)-ord('A')+i)%26+ord('A'))
        else:
            ans+=p
    if "LIVE" in ans and "CHIPMUNKS" in ans:
        print(ans)
        break