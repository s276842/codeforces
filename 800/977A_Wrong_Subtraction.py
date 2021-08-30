#https://codeforces.com/problemset/problem/977/A
import sys

(n,k) = sys.stdin.readline().split()
k = int(k)
while k>0:
    x = int(n[-1])
    if x == 0:
        n = str(int(n)//10)
        k -= 1
    else:
        m = min(x, k)
        k -= m
        x -= m
        n = str(n[:-1]+f'{x}')

print(n)