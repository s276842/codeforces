#https://codeforces.com/problemset/problem/116/A
import sys
n = sys.stdin.readline()

cap = 0
tot = 0
for line in sys.stdin.readlines():

    (a, b) = [int(x) for x in line.split()]
    diff = b-a
    tot += diff
    tot = max(0, tot)

    if tot > cap:
        cap = tot

print(cap)



