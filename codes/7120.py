a = input()
temp = ""
for i in a:
    if temp == "" or temp[-1] != i:
        temp += i
print(temp)
