#https://codeforces.com/problemset/problem/59/A
import sys

s = sys.stdin.readline().strip()

x = -sum([int.from_bytes(c1.encode(), 'little') - int.from_bytes(c2.encode(), 'little') for c1, c2 in zip(s, s.lower())]) // 32

if x > len(s)//2:
    print(s.upper())
else:
    print(s.lower())
