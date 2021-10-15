a = int(input())
b = list(map(int, input().split()))
stat = False
for i in range(2, len(b)):
    if set([b[i-2], b[i], b[i-1]]) == set([2, 1, 0]):
        stat = True
        break
print("TAK" if stat else "NIE")
