b = int(input())
a = [0,1]
stat = True
while True:
    a=[a[-1],(a[-1]+a[-2])]
    if a[-1] == b:
        stat = False
        print(a[-1])
        break
    if a[-1] > b:
        b-=a[-2]
        a = [0,1]