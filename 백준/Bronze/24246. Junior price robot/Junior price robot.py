a = int(input())
b = list(map(int,input().split()))
thing = 0
for i in range(1,len(b)):
    if b[i]<=b[0]:
        thing = i
        break
print("infinity" if not thing else thing)
