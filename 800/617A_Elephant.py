#https://codeforces.com/problemset/problem/617/A
import sys
n = int(sys.stdin.readline())

k = n//5
r = n%5
print(k + (r > 0))