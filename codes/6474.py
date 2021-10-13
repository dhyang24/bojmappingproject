thing = [["A", "A"], ["E", "3"], ["H", "H"], ["I", "I"], ["J", "L"], ["L", "J"], ["M", "M"], ["O", "O"], ["S", "2"], ["T", "T"], [
    "U", "U"], ["V", "V"], ["W", "W"], ["X", "X"], ["Y", "Y"], ["Z", "5"], ["1", "1"], ["2", "S"], ["3", "E"], ["5", "Z"], ["8", "8"]]
while True:
    try:
        a = input()
    except:
        break
    palindrom = a == a[::-1]
    mirrored = ""
    mir = False
    for i in a:
        for p in thing:
            if p[0] == i:
                mirrored += p[1]
    if mirrored[::-1] == a:
        mir = True
    if palindrom and mir:
        print(a, "-- is a mirrored palindrome.")
    elif palindrom:
        print(a, "-- is a palindrome.")
    elif mir:
        print(a, "-- is a mirrored string.")
    else:
        print(a, "-- is not a palindrome.")
    print()
