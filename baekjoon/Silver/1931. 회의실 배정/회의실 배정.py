import sys
si = sys.stdin.readline

n = int(si())

meeting = []
for _ in range(n):
    start, end = map(int, si().split())
    meeting.append((start, end))

meeting.sort(key = lambda x : (x[1], x[0]))

cnt = 1
temp = meeting[0][1]
for i in range(1, n):
    if temp <= meeting[i][0]:
        cnt += 1
        temp = meeting[i][1]

print(cnt)