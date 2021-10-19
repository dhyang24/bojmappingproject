for _ in range(int(input())):
    a,b = map(str,input().split())
    ans = []
    for i in range(len(b)):
        ans.append(chr((ord(b[i])+ord(a[i%len(a)])-(2*ord('A')))%26+ord("A")))
    print("Ciphertext:","".join(ans))