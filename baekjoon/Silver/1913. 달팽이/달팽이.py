import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(si())
target = int(si())
snail = [[0] * n for _ in range(n)]

num, i, x, y = n * n, 0, 0, 0
tx, ty = 0, 0
while num > 0:
    snail[x][y] = num

    if num == target:
        tx, ty = x + 1, y + 1

    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or snail[nx][ny] != 0:
        i = (i + 1) % 4

    x += dx[i]
    y += dy[i]
    num -= 1

for s in snail:
    print(*s)

print(tx, ty)
