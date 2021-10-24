thing = [i for i in range(1,21)]
for i in range(10):
    a,b = map(int,input().split())
    a-=1
    thing = thing[:a]+thing[a:b][::-1]+thing[b:]
print(*thing)
