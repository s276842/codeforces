import sys

(n,k) = [int(x) for x in sys.stdin.readline().split()]
ary = [int(x) for x in sys.stdin.readline().split()]

cnt = 0
flag = True
for x in ary[:k]:
    if x <= 0:
        flag = False
        break
    cnt += 1

if flag:
    for w in ary[k:]:
        if w == x:
            cnt += 1
        else:
            break

print(cnt)
