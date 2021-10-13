import math
while True:
    a = int(input())
    if a == 0:
        break
    ans = [0 for i in range(10)]
    for i in str(math.factorial(a)):
        ans[int(i)]+=1
    print(str(a)+'!',"--")