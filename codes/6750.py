a = input()
stat = True
for i in a:
    if i not in ("I","O","S","H","Z","X","N"):
        stat=False;break
print("YES" if stat else "NO")