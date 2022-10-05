a,b = map(int,input().split())
thing = [i for i in range(1,a+1)]
for i in range(b):
    q,w = map(int,input().split())
    thing[q-1] = w
print(*thing,sep='\n')
