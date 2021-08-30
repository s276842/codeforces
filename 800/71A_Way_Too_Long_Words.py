import sys

n = int(sys.stdin.readline())

for line in sys.stdin:
    if len(line) > 11: #consider \n
        sys.stdout.write(line[0] + f'{len(line)-3}' + line[-2:])
    else:
        sys.stdout.write(line)