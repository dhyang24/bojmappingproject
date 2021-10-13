a = int(input())
for i in range(a):
    print("String #", i+1, sep='')
    thing = []
    for p in input():
        if p != "Z":
            thing.append(chr(ord(p)+1))
        else:
            thing.append("A")
    print(*thing, sep='')
    print()
