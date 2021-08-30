import sys

n = int(sys.stdin.readline())

cnt = 0
for line in sys.stdin:
    x = [int(k) for k in line.split()]
    if sum(x) > 1:
        cnt += 1

print(cnt)