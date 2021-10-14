dic = {"A": 0, "B": 0}
while True:
    a = list(map(str, input().split()))
    if a[0] == '7':
        break
    elif a[0] == '1':
        dic[a[1]] = int(a[2])
    elif a[0] == '2':
        print(dic[a[1]])
    elif a[0] == '3':
        dic[a[1]] = dic[a[1]]+dic[a[2]]
    elif a[0] == '4':
        dic[a[1]] = dic[a[1]]*dic[a[2]]
    elif a[0] == '5':
        dic[a[1]] = dic[a[1]]-dic[a[2]]
    elif a[0] == '6':
        dic[a[1]] = dic[a[1]]//dic[a[2]]
