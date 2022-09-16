from collections import deque

def bfs():                                  # BFS 함수
    q = deque([start])                      # 큐에 시작점 등록
    depth = [0] * 101                       # 탐색 깊이를 저장할 리스트

    visited = [False] * 101                 # 방문 처리를 위한 visited 리스트
    visited[start] = True                   # 시작점 방문 처리

    while q:                                # 큐에 원소가 존재하는 동안
        v = q.popleft()                     # 큐에서 pop하여 현재 노드로 설정
        for nv in edges[v]:                 # 현재 노드와 연결된 다른 노드 확인
            if not visited[nv]:             # 방문하지 않은 노드라면
                visited[nv] = True          # 방문 처리 하고
                depth[nv] = depth[v] + 1    # 해당 노드의 탐색 깊이를 직전 노드의 탐색 깊이 + 1 갑승로!
                q.append(nv)                # 큐에 해당 노드 삽입

    number, max_depth = 0, 0
    for i in range(101):            # 조사한 모든 탐색 깊이에 대해
        if depth[i] >= max_depth:   # 현재까지의 최대 깊이보다 크거나 같을 경우
            max_depth = depth[i]    # 최대 깊이 업뎃하고
            number = i              # 최대 깊이를 가지는 번호 또한 업뎃

    return number   # 최종적으로 최대 깊이를 가지는 가장 큰 번호 리턴


for tc in range(1, 11):
    n, start = map(int, input().split())    # 데이터 길이, 시작점
    data = list(map(int, input().split()))  # 데이터 from-to

    edges = [[] for _ in range(101)]        # 엣지 리스트
    for i in range(0, n, 2):                # 데이터 리스트로부터
        edges[data[i]].append(data[i + 1])  # 엣지 정보 입력

    print(f'#{tc} {bfs()}')