import sys
from collections import deque

# sys.stdin = open('input.txt')
si = sys.stdin.readline

n = int(si())
cards = deque(range(1, n + 1))

while len(cards) > 1:               # 카드가 하나 남을 때까지         
    cards.popleft()                 # 위에거 버리고
    cards.append(cards.popleft())   # 그 다음 거 밑으로 보내 버리기

print(cards[0])
