import sys

# sys.stdin = open('input.txt')
si = sys.stdin.readline

n = int(si())
cards = list(range(1, n + 1))       # 1 ~ n의 카드

results = []                        # 버린 카드 리스트
while len(cards) > 1:               # card가 한 장 남을 때까지
    results.append(cards.pop(0))    # 가장 위 카드 한 장 버리고 버린 카드 리스트에 추가
    cards.append(cards.pop(0))      # 그 다음 카드를 가장 아래로 보내 버리기

print(*results, cards[0])           # 버린 카드 리스트 요소와 마지막 남은 카드 출력
