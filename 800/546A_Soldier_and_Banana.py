#https://codeforces.com/problemset/problem/546/A
import sys

(k,n,w) = [int(x) for x in sys.stdin.readline().split()]

tot = ((w+1)*w/2)*k
print(max(int(tot-n), 0))