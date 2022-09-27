def fastpow(thing,idx,mod):
    if idx == 0:
        return 1
    if idx == 1:
        return thing
    if idx%2 == 0:
        return (fastpow(thing,idx//2,mod)**2)%mod
    else:
        return (fastpow(thing,idx-1,mod)*thing)%mod
def fastpow2(thing,idx,mod):
    ans = 1
    for i in range(len(str(bin(idx)))-3,-1,-1):
        if 2**i&idx:
            ans = (ans*thing)
def getinverse(thing,mod):
    return pow(thing,mod-2,mod)
a,b = map(int,input().split())
ans = 1
mod = 10007
for i in range(b+1,a+1):
    ans= (ans*i)%mod
for i in range(1,a-b+1):
    ans=(ans*getinverse(i,mod))%mod
print(ans)
