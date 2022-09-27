def working(now, depth, visited):   # DFS 함수
    global result

    if now <= result:               # 아직 그다음 직원 일률도 곱 안했는데
        return                      # 현재 결과보다 그 값이 작다면 가망 X

    if depth == n:                  # 모든 직원의 일률을 곱했을 떄
        if now > result:            # 결과값보다 현재 값이 큰 경우만
            result = now            # 갱신
        return

    for i in range(n):              # 재귀적으로 일률 테스트
        if not visited[i]:          # 중복된 인덱스 곱을 받지 위해 방문 처리 안한 곳만
            visited[i] = True       # 방문 처리 후
            working(now * p[depth][i], depth + 1, visited)      # 재귀적으로 함수 실행
            visited[i] = False      # 다시 미방문 처리함으로써 백트래킹


for tc in range(1, int(input()) + 1):
    n = int(input())

    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):          # 모든 일의 성공확률을 계산에 편하게 소수점대로 변환
        for j in range(n):
            p[i][j] /= 100

    visited = [False] * n           # 방문 처리를 위한 visted 리스트
    result = 0                      # 결과값 저장을 위한 변수

    working(1, 0, visited)          # 현재 확률 1, 깊이 0으로 함수 시작
    result *= 100

    print(f'#{tc} {result:.6f}')