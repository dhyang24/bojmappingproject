import math
ans = 0
print("n e")
print("- -----------")
for i in range(0, 10):
    ans += (1/math.factorial(i))
    if i == 0:
        print(0, 1)
    elif i == 1:
        print(1, 2)
    elif i == 2:
        print(2, 2.5)
    else:
        print(i, "{:.9f}".format(ans))
