import sys
from collections import deque
si = sys.stdin.readline

k = int(si())
stk = deque()

for _ in range(k):
    num = int(si())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))