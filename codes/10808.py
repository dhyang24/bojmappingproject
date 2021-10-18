a = input()
b = [0 for i in range(26)]
for i in range(len(a)):
    b[ord(a[i])-ord('a')]+=1
print(*b)