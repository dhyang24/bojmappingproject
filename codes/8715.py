a = int(input())
print("TAK" if sorted(list(map(int,input().split()))) == [i+1 for i in range(a)] else "NIE")