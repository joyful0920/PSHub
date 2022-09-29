import sys
si = sys.stdin.readline


def find_parent(x):      # 파인드 연산
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):  # 유니온 연산
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(si())                # 컴퓨터 수
m = int(si())                # 연결 선 수
parent = list(range(n + 1))  # 부모 테이블 생성 및 자기 자신으로 초기화

edges = []
for _ in range(m):
    a, b, cost = map(int, si().split())
    edges.append((cost, a, b))  # 엣지 정보를 비용과 함께 튜플로 묶어 저장
edges.sort()                    # 비용 기준 오름차순 정렬!

result, cnt = 0, 0              # 최종 비용을 저장할 결과 변수 & MST를 만드는 데 사용한 간선 수 변수
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):    # 두 노드의 루트가 다르다면 싸이클 발생 X
        union_parent(a, b)                  # 유니온~
        result += cost                      # 비용 더해주고
        cnt += 1                            # 카운트도!

    if cnt >= n - 1:    # MST가 완성됐다면
        break           # 더 이상 간선 확인할 필요 X

print(result)