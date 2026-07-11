import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline


def check(first, second):
    cnt = 0
    for i in range(x, x + 8, 2):
        for j in range(y, y + 8, 2):
            if board[i][j] != first:
                cnt += 1
        for j in range(y + 1, y + 8, 2):
            if board[i][j] != second:
                cnt += 1
    for i in range(x + 1, x + 8, 2):
        for j in range(y, y + 8, 2):
            if board[i][j] != second:
                cnt += 1
        for j in range(y + 1, y + 8, 2):
            if board[i][j] != first:
                cnt += 1

    return cnt


n, m = map(int, si().split())
board = [si().rstrip() for _ in range(n)]

result = float('inf')
for x in range(n - 8 + 1):
    for y in range(m - 8 + 1):
        cnt = min(check('W', 'B'), check('B', 'W'))
        if cnt < result:
            result = cnt

print(result)
