while True:
    a = input()
    if a == "ENDOFINPUT":
        break
    b = input()
    ans = ""
    for i in b:
        if ord(i) >= ord("A") and ord(i) <= ord("Z"):
            ans+=chr((ord(i)-ord("A")-5)%26+ord("A"))
        else:
            ans+=i
    print(ans)
    c = input()
