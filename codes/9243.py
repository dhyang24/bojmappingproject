q = int(input())
a = input()
b = input()
if q%2:
    stat = True
    for i in range(len(a)):
        if a[i] == b[i]:
            stat = False
            break
    if stat:
        print("Deletion succeeded")
    else:
        print("Deletion failed")    
else:
    if a == b:
        print("Deletion succeeded")
    else:
        print("Deletion failed")