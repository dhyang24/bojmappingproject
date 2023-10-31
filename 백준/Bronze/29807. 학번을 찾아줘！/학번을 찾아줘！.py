t = int(input())
z = list(map(int,input().split()))
q = z[0]
try:
    w = z[1]
except:
    w = 0
try:
    e = z[2]
except:
    e = 0
try:
    r = z[3]
except:
    r = 0
try:
    t = z[4]
except:
    t = 0
ans = 0
if q > e:
    ans+=508*(q-e)
else:
    ans+=108*(e-q)
if w > r:
    ans+=212*(w-r)
else:
    ans+=305*(r-w)
ans+=t*707
print(ans*4763)
