import math
while True:
    a = int(input())
    if a == 0:
        break
    garbage = input()
    ans = [0 for i in range(10)]
    for i in str(math.factorial(a)):
        ans[int(i)] += 1
    print(str(a)+'!', "--")
    print("   (0)"+" "*(5-len(str(ans[0])))+str(ans[0])+"    (1)"+" "*(5-len(str(ans[1])))+str(ans[1])+"    (2)"+" "*(5-len(
        str(ans[2])))+str(ans[2])+"    (3)"+" "*(5-len(str(ans[3])))+str(ans[3])+"    (4)"+" "*(5-len(str(ans[4])))+str(ans[4]))
    print("   (5)"+" "*(5-len(str(ans[5])))+str(ans[5])+"    (6)"+" "*(5-len(str(ans[6])))+str(ans[6])+"    (7)"+" "*(5-len(
        str(ans[7])))+str(ans[7])+"    (8)"+" "*(5-len(str(ans[8])))+str(ans[8])+"    (9)"+" "*(5-len(str(ans[9])))+str(ans[9]))
