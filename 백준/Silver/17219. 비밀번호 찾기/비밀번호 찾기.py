import sys
input = sys.stdin.readline
print = sys.stdout.write
a,b=map(int,input().split())
dic = {}
for i in range(a):
    q,w = map(str,input().split())
    dic[q]=w
for i in range(b):
    print(dic[input().strip()]+'\n')
