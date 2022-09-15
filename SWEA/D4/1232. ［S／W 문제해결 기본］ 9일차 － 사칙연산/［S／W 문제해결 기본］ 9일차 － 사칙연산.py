def cal(c):                 # 사칙연산 함수
    b = nums.pop()          # a 와 b를 숫자 스택에서 pop
    a = nums.pop()

    if c == '+':
        nums.append(a + b)
    elif c == '-':
        nums.append(a - b)
    elif c == '*':
        nums.append(a * b)
    else:
        nums.append(a // b)


def postorder(v):                           # 계산을 위해 후위 순회
    if v != 0:
        postorder(tree[0][v])
        postorder(tree[1][v])
        if tree[2][v].isdigit():            # 노드 값이 숫자라면
            nums.append(int(tree[2][v]))    # 연산에 사용할 숫자 스택에 넣어주기
        else:                               # 연산자라면
            cal(tree[2][v])                 # 연산 함수 수행


for tc in range(1, 11):
    n = int(input())
    tree = [[0] * (n + 1) for _ in range(3)]        # 왼쪽 자식 노드, 오른쪽 자식 노드, 노드 값 리스트

    for _ in range(n):                              
        info = list(input().split())                # 노드 정보 입력 받고

        tree[2][int(info[0])] = info[1]             # 해당 노드 번호에 노드 값 저장
        if not info[1].isdigit():                   # 노드 값이 연산자라면
            tree[0][int(info[0])] = int(info[2])    # 자식 노드들 등록
            tree[1][int(info[0])] = int(info[3])

    nums = []
    postorder(1)
    print(f'#{tc} {nums[-1]}')