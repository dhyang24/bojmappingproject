mx =100
su = 100
for i in range(int(input())):
    su+=int(input())
    mx = max(su,mx)
print(mx)