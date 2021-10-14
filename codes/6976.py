for _ in range(int(input())):
    a = int(input())
    z = a
    print(a)
    while len(str(a)) > 2:
        a = int(str(a)[:-1])-int(str(a)[-1])
        print(a)
    print("The number",z,("is divisible by 11." if a%11 == 0 else "is not divisible by 11."))
    print()