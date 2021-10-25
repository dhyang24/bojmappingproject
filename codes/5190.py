for qwer in range(int(input())):
    a,b = map(float,input().split())
    c = []
    for i in range(int(a)):
        c.append(list(map(float,input().split())))
        b+=c[-1][0]
    speed = 0
    distance = 0
    for i in c:
        acc = i[2]/b-9.81
        distance = distance+(speed*i[1]+(1/2)*acc*(i[1]**2))
        speed = speed + acc*i[1]
        b-=i[0]
    print("Data Set "+str(qwer+1)+":")
    print("{:.2f}".format(distance))