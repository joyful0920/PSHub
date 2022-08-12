import sys

word = sys.stdin.readline().rstrip()

for c in word:
    if c not in 'CAMBRIDGE':
        print(c, end='')
        