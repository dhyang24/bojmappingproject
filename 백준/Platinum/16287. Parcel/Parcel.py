a,b=map(int,input().split());c=list(map(int,input().split()));d=[0,0,0,0]
for i in c:d=[d[0]|(1<<i),d[1]|(d[0]<<i),d[2]|(d[1]<<i),d[3]|(d[2]<<i)]
print("YES"if d[3]&(1<<a) else"NO")