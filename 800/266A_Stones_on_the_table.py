#https://codeforces.com/problemset/problem/266/A
import sys

sys.stdin.readline()

s = sys.stdin.readline()
cnt = 0
i = 0
while i < len(s)-1:
    c = s[i]
    j = i+1
    while j < len(s)-1 and s[j] == c:
        cnt += 1
        j+=1
    i = j

print(cnt)