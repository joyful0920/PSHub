def inorder(v):             # 중위 순회 함수
    global result
    if v:                   # 노드인 경우
        inorder(ch1[v])     # 왼쪽 자식 노드 방문하고
        result += nodes[v]  # 부모 노드 방문의 의미로 결과 문자열에 해당 노드 문자 붙여주기
        inorder(ch2[v])     # 마지막으로 오른쪽 노드 방문


for tc in range(1, 11):
    n = int(input())    # 노드 수
    e = n - 1           # 간선 수

    ch1 = [0] * (n + 1)     # 왼쪽 자식 노드 리스트
    ch2 = [0] * (n + 1)     # 오른쪽 자식 노드 리스트
    nodes = [0]             # 노드 문자 리스트
    for _ in range(n):
        info = list(input().split())    # 노드 정보를 리스트로 입력 받아
        nodes.append(info[1])           # 노드 문자 등록

        if len(info) > 2:                           # 자식 노드가 있는 경우만
            ch1[int(info[0])] = int(info[2])        # 왼쪽 자식 노드 먼저 등록
            if len(info) > 3:                       # 오른쪽 자식 노드도 있다면
                ch2[int(info[0])] = int(info[3])    # 예아~
    
    result = ''     # 결과 문자열
    inorder(1)      # 1을 루트로 중위 순회 수행
    print(f'#{tc} {result}')
