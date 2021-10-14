while True:
    a = input()
    if a == "0+0=0":
        print("True")
        break
    a, b = a.split("+")
    b, c = b.split("=")
    a = a[::-1]
    b = b[::-1]
    c = c[::-1]
    if int(a) + int(b) == int(c):
        print("True")
    else:
        print("False")
