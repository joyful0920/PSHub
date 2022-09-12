for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for j in range(n):
        temp = 0                        # 마지막으로 확인한 자성체 종류를 자장시킬 변수
        for i in range(n):
            if table[i][j] != 0:        # 자성체가 존재하는 칸이고
                if table[i][j] == 2:    # S극이라면
                    if temp == 1:       # 마지막 확인한 자성체가 N극일 때만
                        cnt += 1        # 교착 상태 수 + 1
                temp = table[i][j]      # 마지막 확인한 자성체 종류 업뎃

    print(f'#{tc} {cnt}')