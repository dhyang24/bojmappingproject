a = int(input())
thing = []
thing2 = []
b = list(map(int,input().split()))
for i in range(len(b)):
    if b[i] == 1:
        thing.append(i)
    else:
        thing2.append(i)
print(max(max(thing)-min(thing2),max(thing2)-min(thing)))