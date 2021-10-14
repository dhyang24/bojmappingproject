while True:
    a = int(input())
    if a == 0:
        break
    thing = [a]
    while True:
        b = a**2
        b = (b % 1000000//100)
        if b in thing:
            break
        thing.append(b)
        a = b
    print(len(thing))
