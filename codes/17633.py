import sys
import random
import math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
 
def power(x, y, n):
    ans = 1
    x = x % n
    while y > 0:
        if y & 1:
            ans = (ans * x) % n
        y = y >> 1
        x = (x*x) % n
    return ans
 
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
 
def miller_rabin(n, a):
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d = d//2

    x = power(a, d, n)
    if x == 1 or x == n-1:
        return True

    for i in range(r-1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False

def is_prime(n):
    global divisors
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for a in alist:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True
 
 
def pollardRho(n):
    if is_prime(n):
        if n%4 == 3:
            try:
                divisors[n]+=1
            except:
                divisors[n]=1
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        pollardRho(n//2)
        return 0
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            pollardRho(n)
            return 0
    if is_prime(d):
        if d%4 == 3:
            try:
                divisors[d]+=1
            except:
                divisors[d]=1
        pollardRho(n//d)
        return 0
    else:
        pollardRho(d)
        pollardRho(n//d)
        return 0
while n%4 == 0:
    n=n//4
if n%8 == 7:
    print('4\n')
else:
    ans = 0
    divisors = {}
    pollardRho(n)
    for i in divisors.keys():
        if divisors[i]%2:
            ans=1
            break
    if ans:
        print('3\n')
    else:
        if n == int(math.sqrt(n))**2:
            print('1\n')
        else:
            print('2\n')
        
