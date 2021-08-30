#https://codeforces.com/problemset/problem/791/A
import sys

(a, b) = [int(x) for x in sys.stdin.readline().split()]

x = b - a
k = 1
c = 1
cnt = 1
while c*a - (1 << k)*x <= 0:
    c =(c* 3) +(1 << k)
    k += 1
    cnt += 1

print(cnt)