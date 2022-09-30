def find_parent(x):     # 파인드 연산
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b): # 유니온 연산
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for tc in range(1, int(input()) + 1):
    n = int(input())                        # 섬 수
    x = list(map(int, input().split()))     # x 좌표 리스트
    y = list(map(int, input().split()))     # y 좌표 리스트
    e = float(input())                      # 세율

    edges = []                              # 엣지 리스트
    for i in range(n):
        for j in range(n):                  # 가중치를 계산하여
            cost = e * (abs(x[i] - x[j]) ** 2 + abs(y[i] - y[j]) ** 2)
            edges.append((cost, i, j))      # 가중치 순으로 엣지 리스트에 등록
    edges.sort()

    parent = list(range(n))                     # 부모 테이블 생성 및 자기 자신으로 초기화

    result, cnt = 0.0, 0                        # 결과 변수, 카운트 변수
    for edge in edges:
        c, a, b = edge                          # 엣지를 하나씩 확인하며
        if find_parent(a) != find_parent(b):    # 사이클이 발생하지 않을 때만
            union_parent(a, b)                  # 유니온 연산 진행하여 MST에 포함
            result += c                         # 포함 시켰으면 MST 전체 가중치 늘려주고
            cnt += 1                            # 카운트 + 1

        if cnt >= n - 1:                        # MST가 완성됐다면
            break                               # 브렉끼해서 불필요한 연산 X

    print(f'#{tc} {result: .0f}')               # 소수 첫째 자리에서 반올림하여 결과 출력