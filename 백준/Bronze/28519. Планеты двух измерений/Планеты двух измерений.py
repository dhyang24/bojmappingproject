a,b = map(int,input().split())
print(min(a,b)+min(max(a,b),min(a,b)+1))