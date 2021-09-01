#https://codeforces.com/problemset/problem/266/B
import sys

(n,t) = [int(x) for x in sys.stdin.readline().split()]

s = list(sys.stdin.readline().strip())

for i in range(t):
    b_pos = [i for i, c in enumerate(s[:-1]) if c == 'B']
    for j in b_pos:
        c_next = s[j+1]
        if c_next == 'G':
            s[j], s[j+1] = s[j+1], s[j]

print(''.join(s))