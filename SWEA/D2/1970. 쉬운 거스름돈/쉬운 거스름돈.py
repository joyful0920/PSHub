t = int(input())
for tc in range(1, t + 1):
    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnts = [0] * 8                      # 동전 종류와 그 카운트 리스트의 인덱스가 매칭되게

    money = int(input())
    for i in range(8):
        if money >= coins[i]:           # 큰 금액부터 거슬러 주기 -> 최소 개수
            cnts[i] = money // coins[i] # 남은 돈을 현재 동전 종류로 나눈 몫 -> 가능한 동전 수
            money %= coins[i]           # 그 나머지를 남은 돈으로 새로게 저장

    print(f'#{tc}')
    print(*cnts)