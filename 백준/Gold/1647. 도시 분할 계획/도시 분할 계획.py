import sys
si = sys.stdin.readline

# find 연산 함수
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 개수 N과 길의 개수 M 입력
n, m = map(int, si().split())

# 부모 테이블 생성 및 자기 자신으로 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# 간선(마을 사이 길)을 담을 리스트
edges = []
# 최종 유지비를 담을 변수
result = 0
# 신장 트리에 포함되는 간선 중 가장 큰 비용을 담을 변수
max_c = 0

# 모든 길 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, si().split())
    edges.append((a, b, c))

# 간선을 유지비순으로 정렬
edges.sort(key=lambda x:x[2]) # lambda

# 간선 확인
for edge in edges:
    a, b, c = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        max_c = c

print(result - max_c)