s, t = 0, 0
for i in range(int(input())):
    for q in input():
        if q == 's' or q == 'S':
            s += 1
        if q == 't' or q == 'T':
            t += 1
if s == t:
    print("French")
elif s < t:
    print("English")
else:
    print("French")
