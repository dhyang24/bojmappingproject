import math
import sys
input = sys.stdin.readline
print = sys.stdout.write
def merge(a,b):
    return a+b
def init(node,s,e):
    global tree
    global data
    if s == e:
        tree[node-1] = data[s]
        return tree[node-1]
    tree[node-1] = merge(init(node*2,s,(s+e)//2),init(node*2+1,(s+e)//2+1,e))
    return tree[node-1]
def lazydo(node,s,e):
    global lazy
    if lazy[node-1] != 0:
        tree[node-1] += (e-s+1)*lazy[node-1]
        if s != e:
            lazy[node*2-1]+=lazy[node-1]
            lazy[node*2]+=lazy[node-1]
        lazy[node-1] = 0
def lazyfind(node,s,e,s1,e1):
    global tree
    lazydo(node,s,e)
    if e < s1 or s > e1:
        return 0
    if s >= s1 and e <= e1:
        return tree[node-1]
    return merge(lazyfind(node*2,s,(s+e)//2,s1,e1),lazyfind(node*2+1,(s+e)//2+1,e,s1,e1))
def lazyupdate(node,s,e,s1,e1,diff):
    lazydo(node,s,e)
    if e < s1 or s > e1:
        return 0
    if s >= s1 and e <= e1:
        tree[node-1] += (e-s+1)*diff
        if s!=e:
            lazy[node*2-1] +=diff
            lazy[node*2]+=diff
        return 0
    lazyupdate(node*2,s,(s+e)//2,s1,e1,diff)
    lazyupdate(node*2+1,(s+e)//2+1,e,s1,e1,diff)
    tree[node-1] = tree[node*2-1]+tree[node*2]
def find(node,s,e,s1,e1):
    global tree
    if e < s1 or s > e1:
        return 0
    if s >= s1 and e <= e1:
        return tree[node-1]
    return merge(find(node*2,s,(s+e)//2,s1,e1),find(node*2+1,(s+e)//2+1,e,s1,e1))
le = int(input())
ini = 0
data = [0]+list(map(int,input().split()))
for i in range(2**math.ceil(math.log2(le))-le):
    data.append(ini)
tree = [ini for i in range(2**(math.ceil(math.log2(le))+1)-1)]
treele = 2**math.ceil(math.log2(le))-1
lazy = [0 for i in range(len(tree))]
for i in range(le):
    lazyupdate(1,1,le,i+1,i+1,data[i+1]-data[i])
for i in range(int(input())):
    a = list(map(int,input().split()))
    if a[0] == 1:
        lazyupdate(1,1,le,a[1],a[2],1)
        lazyupdate(1,1,le,a[2]+1,a[2]+1,(a[1]-a[2]-1))
    else:
        print(str(lazyfind(1,1,le,1,a[1]))+'\n')
