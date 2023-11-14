data = [[0 for i in range(101)] for i in range(101)]
ans = 0
for i in range(int(input())):
    q,w=map(int,input().split())
    for i in range(q,q+10):
        for j in range(w,w+10):
            if not data[i][j]:ans+=1
            data[i][j] = 1
print(ans)

