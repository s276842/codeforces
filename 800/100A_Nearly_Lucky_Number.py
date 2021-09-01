#https://codeforces.com/problemset/problem/110/A
import sys
import re

s = sys.stdin.readline().strip()
n = len(re.findall('4|7', s))

if n == 4 or n == 7:
    print("YES")
else:
    print("NO")