import sys

croatian_letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = sys.stdin.readline().rstrip()
cnt = 0

while len(word) > 0:
    cnt += 1
    if word[:3] in croatian_letters:
        word = word[3:]
    elif word[:2] in croatian_letters:
        word = word[2:]
    else:
        word = word[1:]

print(cnt)