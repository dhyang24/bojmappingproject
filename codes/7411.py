import sys
input = sys.stdin.readline
print = sys.stdout.write
a = input().strip()
b = input().strip()
stat = len(a)//2
ans = ''
temp = ord(" ")
for i in range(stat):
    thing = int(b[i*2:i*2+2],16)^temp
    ans+='0'+hex(thing)[2:] if len(hex(thing)[2:]) == 1 else hex(thing)[2:]
    temp = thing^int(a[i*2:i*2+2],16)
ans+=hex(int(b[-2:-1]+b[-1],16)^temp)[2:]
print(ans.upper())