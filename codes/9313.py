while True:
    a = int(input())
    if a == -1:
        break
    print(int('{:032b}'.format(a)[::-1],2))