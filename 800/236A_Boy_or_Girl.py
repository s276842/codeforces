#https://codeforces.com/problemset/problem/236/A
import sys
name = sys.stdin.readline().strip()
s = set(name)

if len(s) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")