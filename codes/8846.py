ans = 0
temp = 1
for i in range(int(input())):
    ans= (ans+temp)%500000009
    temp= (temp*4)%500000009
print(ans)