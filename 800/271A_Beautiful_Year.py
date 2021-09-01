#https://codeforces.com/problemset/problem/271/A
import sys

s = sys.stdin.readline().strip()

for i in range(len(s)-1, -1, -1):
    n = int(s[i])
    set_year = set([int(x) for x in s[:i+1]])

    if len(set_year) != len(s[:i+1]):
        continue

    set_available = set(range(int(s[i]), 10))

    set_available -= set_year

    if len(set_available) > 0 and len(set_year) == len(s[:i+1]):

        k = min(set_available)
        new_year = s[:i] + f'{k}'
        set_available.add(int(s[i]))
        set_available.add(0)
        set_available -= set([int(x) for x in new_year])

        for j in range(i + 1, len(s)):
            k = min(set_available)
            new_year += f'{k}'
            set_available.add(int(s[j]))
            set_available -= set([int(x) for x in new_year])

        break
print(new_year)