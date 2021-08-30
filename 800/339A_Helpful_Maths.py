#https://codeforces.com/problemset/problem/339/A
import sys

s = sys.stdin.readline()
s = s.replace('+', '')

n = [0]*3
for c in s[:-1]:
    n[int(c)-1] +=1

out_s = "1+" * n[0] + "2+" * n[1] + "3+"*n[2]
print(out_s[:-1])
