a = int(input())
print(chr(ord("A")+(a-184) % 12), (a-184) % 10, sep='')
