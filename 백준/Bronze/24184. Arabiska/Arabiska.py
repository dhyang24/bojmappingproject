a = int(input())
b = input()
ans = ''
for i in range(len(b)):
    if i<len(b)-2 and b[i] in ['a','e','i','o','u','y'] and b[i+1] not in ['a','e','i','o','u','y',' '] and b[i+2] not in ['a','e','i','o','u','y',' ']:
        continue
    else:
        ans+=b[i]
print(ans[::-1])