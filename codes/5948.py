a = int(input())
visited = [a]
now = 0
while True:
    now += 1
    temp = a % 1000//10
    a = temp**2
    if a in visited:
        break
    visited.append(a)
print(now)
