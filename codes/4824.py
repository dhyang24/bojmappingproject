while True:
    a,b,c = sorted(map(float,input().split()),reverse = True)
    if (a,b,c) == (0,0,0):
        break
    if a >= 125 and a <= 290 and b >= 90 and b <= 155 and c >= 0.25 and c <= 7:
        print("letter")
    elif a >= 125 and b >= 90 and c>=0.25 and (a >= 290 or b >=155 or c>=7) and a<=380 and b <= 300 and c <=50:
        print("packet")
    elif a >= 125 and b >= 90 and c >= 0.25 and (a >= 380 or b >= 300 or c >= 50) and a+(b+c)*2 <= 2100:
        print("parcel")
    else:
        print("not mailable")