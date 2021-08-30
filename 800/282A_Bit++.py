# https://codeforces.com/problemset/problem/282/A

import sys

n = int(sys.stdin.readline())

x = 0
for line in sys.stdin:
    line = line.replace('X', '')

    if line[:-1] == '++':
        x += 1
    else:
        x -= 1

print(x)