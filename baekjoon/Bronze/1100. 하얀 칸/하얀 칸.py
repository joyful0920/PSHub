import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline

chess = [si().rstrip() for _ in range(8)]

result = 0
for i in range(8):
    if not i % 2:
        for j in range(0, 8, 2):
            if chess[i][j] == 'F':
                result += 1
    else:
        for j in range(1, 8, 2):
            if chess[i][j] == 'F':
                result += 1

print(result)
