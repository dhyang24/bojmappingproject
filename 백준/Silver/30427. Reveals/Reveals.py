import sys
a = input()
b = int(input())
c = []
for i in range(b):
    c.append(input())
d = int(input())
e1 = {}
for i in range(d):
    q = input()
    e1[q] = 1
cnt = {}
if 'dongho' in c:
    print("dongho")
    sys.exit()
for i in c:
    if not e1.get(i):
        cnt[i] = 1
if len(cnt) == 0:
    print("swi")
else:
    if cnt.get("bumin"):
        print("bumin")
    elif cnt.get("cake"):
        print("cake")
    elif cnt.get("lawyer"):
        print("lawyer")
    else:
        cnt = sorted(list(cnt))
        print(cnt[0])