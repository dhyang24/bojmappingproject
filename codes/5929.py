a = input()
b = input()
num = []
for i in range(len(a)):
    num.append(int(a[:i]+str(1 if a[i] == '0' else 0)+a[i+1:], 2))
for i in range(len(b)):
    thing = []
    if b[i] != '1':
        if int(b[:i]+'1'+b[i+1:], 3) in num:
            print(int(b[:i]+'1'+b[i+1:], 3))
            break
    if b[i] != '2':
        if int(b[:i]+'2'+b[i+1:], 3) in num:
            print(int(b[:i]+'2'+b[i+1:], 3))
            break
    if b[i] != '0':
        if int(b[:i]+'0'+b[i+1:], 3) in num:
            print(int(b[:i]+'0'+b[i+1:], 3))
            break
