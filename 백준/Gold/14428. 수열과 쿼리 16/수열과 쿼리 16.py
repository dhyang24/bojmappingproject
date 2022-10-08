import sys
import math
from collections import deque
def find(layer,number,s,e,l,r):
    global q
    global tree
    if l > e or r < s:
        return len(q)-1
    if l <= s and r >= e:
        return tree[layer][number][0]
    m = (s+e)//2
    if layer == 0:
        return len(q)-1
    left = find(layer-1, number*2,s,m,l,r)
    right = find(layer-1, number*2+1,m+1,e,l,r)
    return merge([left],[right])[0]
def merge(a,b):
    global q
    a,b = sorted([a,b],key= lambda k:k[0])
    if q[a[0]]<= q[b[0]]:
        return [a[0]]
    else:
        return [b[0]]
input = sys.stdin.readline
print = sys.stdout.write
le = int(input())
q = list(map(int,input().split()))
qwert = int(input())
tree = []
for i in range(math.ceil(math.log(le,2))+1):
    temp = []
    if tree:
        for p in range(len(tree[-1])//2):
            temp.append(merge(tree[-1][p*2+1],tree[-1][p*2]))
        if len(tree[-1])%2 == 1:
            temp.append(tree[-1][-1])
    else:
        temp = [[i] for i in range(len(q))]
        temp+=[[len(q)]]*(2**math.ceil(math.log(le,2))-le)
        q.append(10000000000)
    tree.append(temp)
for _ in range(qwert):
    a,b,c = map(int,input().split())
    if a == 1:
        b-=1
        for i in range(len(tree)):
            if i == 0:
                q[b] = c
                continue
            temp = (b>>(i-1))-((b>>(i-1))%2)
            if (temp+1) >= len(tree[i-1]):
                tree[i][b>>i] = tree[i-1][b>>(i-1)]
            else:
                tree[i][b>>i] = merge(tree[i-1][temp],tree[i-1][temp+1])
    if a == 2:
        stat = 0
        ans = 0
        bans = 0
        b,c = sorted([b,c])
        print(str(find(len(tree)-1,0,0,len(tree[0])-1,b-1,c-1)+1)+'\n')