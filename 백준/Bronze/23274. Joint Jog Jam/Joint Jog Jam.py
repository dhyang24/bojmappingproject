a,b,c,d,e,f,g,h = list(map(int,input().split()))
print(max(((a-c)**2+(b-d)**2)**0.5,((e-g)**2+(f-h)**2)**0.5))

