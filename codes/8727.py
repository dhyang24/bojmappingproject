a, b, c = map(int, input().split())
q = []
for i in range(6):
    q.append(int(input()))
z, x, v = q[4]+(q[5]*0.5+q[3]*0.5), q[0] + \
    (q[1]*0.5+q[5]*0.5), q[2]+(q[3]*0.5+q[1]*0.5)
a, b, c = (max(0, z-a), max(0, x-b), max(0, v-c))
print(int(a) if a == int(a) else a, int(b) if b ==
      int(b) else b, int(c) if c == int(c) else c)
