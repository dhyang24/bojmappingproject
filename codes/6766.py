a = int(input())
b = input()
ans = []
for i in range(len(b)):
    s = 3*(i+1)+a
    ans.append(chr((ord(b[i])-ord('A')-s) % 26+ord("A")))
print(*ans, sep='')
