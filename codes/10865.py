a,b = map(int,input().split())
thing = [0 for i in range(a)]
for i in range(b):
    q,w = map(int,input().split())
    thing[q-1]+=1
    thing[w-1]+=1
for i in thing:
    print(i)