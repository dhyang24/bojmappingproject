cnt = 0
while True:
    try:
        a = input()
    except:
        break
    for i in range(3,len(a)):
        if a[i-3]+a[i-2]+a[i-1]+a[i] == 'joke':
            cnt+=1
print(cnt)