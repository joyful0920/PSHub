for tc in range(1, 11):
    n = int(input())
    magnetics = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for j in range(n):
        now = 0
        for i in range(n):              # 열 우선 순회
            if magnetics[i][j] == 2:    # n극이 등장
                if now == 1:            # s극이 등장한 적이 있다면
                    result += 1         # 교착 상태 + 1
            if magnetics[i][j] != 0:    # 자석을 만나면
                now = magnetics[i][j]   # now에 해당 극 저장

    print(f'#{tc} {result}')