#https://codeforces.com/problemset/problem/263/A
import sys
import math

for i,line in enumerate(sys.stdin):
    for j,x in enumerate(line.split()):
        if int(x) == 1:
            print(int(math.fabs(j - 2)) + int(math.fabs(i - 2)))