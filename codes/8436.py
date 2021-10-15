a = input()
ans = 1
for i in a:
    if i in ("T", "D", "L", "F"):
        ans *= 2
print(ans)
