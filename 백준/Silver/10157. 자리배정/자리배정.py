import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

c, r = map(int, si().split())
target = int(si())

if target > c * r:
    print(0)
else:
    stadium = [[0] * c for _ in range(r)]

    num, i = 1, 0
    x, y = 0, 0

    while num <= c * r:
        stadium[x][y] = num

        if num == target:
            print(y + 1, x + 1)
            break

        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or stadium[nx][ny] != 0:
            i = (i + 1) % 4

        x += dx[i]
        y += dy[i]
        num += 1
