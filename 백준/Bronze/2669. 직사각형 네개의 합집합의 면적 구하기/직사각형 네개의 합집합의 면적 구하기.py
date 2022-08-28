import sys
si = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
cnt = 0

for _ in range(4):
    lx, ly, rx, ry = map(int, si().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            if arr[i][j] == 0:
                cnt += 1
                arr[i][j] = 1

print(cnt)
