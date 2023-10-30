ans = 0
for i in range(8):
    for j in input():
        if j == "P":
            ans+=1
        elif j == "p":
            ans-=1
        elif j == "N" or j == "B":
            ans+=3
        elif j == "n" or j == "b":
            ans-=3
        elif j == "R":
            ans+=5
        elif j == "r":
            ans-=5
        elif j == "Q":
            ans+=9
        elif j == "q":
            ans-=9
print(ans)