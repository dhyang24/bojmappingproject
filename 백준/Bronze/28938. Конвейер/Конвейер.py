a = int(input())
b = list(map(int,input().split()))
if sum(b)>0:
    print("Right")
elif sum(b)<0:
    print("Left")
else:
    print("Stay")