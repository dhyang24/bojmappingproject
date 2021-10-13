a = []
for i in range(int(input())):
    a.append(int(input()))
avg = sum(a)//len(a)
thing = 0
for i in a:
    thing += abs(avg-i)
print(thing//2)
