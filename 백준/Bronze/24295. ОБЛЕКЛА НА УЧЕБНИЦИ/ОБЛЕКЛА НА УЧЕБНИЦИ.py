a,b,c,d = map(int,input().split())
thing = sorted((a*10+b,c*10+d))
a,b,c,d = map(int,input().split())
thing2 = sorted((a*10+b,c*10+d))
a,b,c,d = map(int,input().split())
thing3 = sorted((a*10+b,c*10+d))
if thing2[0] >= thing[0]+10 and thing2[1] >= thing[1] and thing3[1] >= thing[1] and thing3[0] >= thing[0]+10:
    if thing2[0] < thing3[0]:
        print(1)
        print("{:.01f}".format(thing2[0]/10),"{:.01f}".format(thing2[1]/10))
    else:
        print(2)
        print("{:.01f}".format(thing3[0]/10),"{:.01f}".format(thing3[1]/10))
elif thing2[0] >= thing[0]+10 and thing2[1] >= thing[1]:
    print(1)
    print("{:.01f}".format(thing2[0]/10),"{:.01f}".format(thing2[1]/10))
elif thing3[1] >= thing[1] and thing3[0] >= thing[0]+10:
    print(2)
    print("{:.01f}".format(thing3[0]/10),"{:.01f}".format(thing3[1]/10))
else:
    print(0)
