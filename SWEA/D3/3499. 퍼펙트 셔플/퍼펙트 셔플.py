t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cards = list(map(str, input().split()))

    mid = n // 2                        # 절반으로 나눌 중간 인덱스
    if n % 2:                           # 카드가 홀수 장인 경우
        up = cards[:mid + 1]            # 윗 덱을 한장 더 많게
        down = cards[mid + 1:]
    else:
        up = cards[:mid]
        down = cards[mid:]

    print(f'#{tc}', end=' ')
    for i in range(mid):                # 윗 덱과 아랫 덱을 번갈아 출력
        print(up[i], down[i], end=' ')

    if n % 2:                           # 홀수 장이었던 경우는
        print(up[mid])                  # 윗덱 마지막 카드까지
    else:
        print()