#https://codeforces.com/problemset/problem/112/A
import sys

s1 = sys.stdin.readline().lower()
s2 = sys.stdin.readline().lower()

if s1 == s2:
    print(0)
elif s1 > s2:
    print(1)
else:
    print(-1)