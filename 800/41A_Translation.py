import sys

s1=  sys.stdin.readline().strip()
s2=  sys.stdin.readline().strip()

if s1 == s2[::-1]:
    print("YES")
else:
    print("NO")