import sys

s = sys.stdin.readline().rstrip()

left, right = 0, 0
standard = s.index('0')

for c in s[:standard]:
    if c == '@':
        left += 1

for c in s[standard:]:
    if c == '@':
        right += 1

print(left, right)
