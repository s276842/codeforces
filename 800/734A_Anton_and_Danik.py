#https://codeforces.com/problemset/problem/734/A
import sys
import re

n = sys.stdin.readline()
s = sys.stdin.readline().strip()

n_a = len(re.findall('A', s))
n_d = len(re.findall('D', s))

if n_a > n_d:
    print('Anton')
elif n_a == n_d:
    print('Friendship')
else:
    print('Danik')