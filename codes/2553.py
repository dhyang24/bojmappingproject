import math
a = int(input())
thing = str((2**(a//5)*math.factorial(a//5) * math.factorial(a%5)))
for i in range(len(thing)):
    if thing[-i-1] != '0':
        print(thing[-i-1])
        break
