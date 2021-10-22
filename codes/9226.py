while True:
    a = input()
    if a == "#":
        break
    if 'a' not in a and 'e' not in a and 'i' not in a and 'o' not in a and 'u' not in a: print(a+'ay')
    else:
        po = 0
        while a[po] not in ['a','e','i','o','u']:
            po+=1
        print(a[po:]+a[:po]+'ay')