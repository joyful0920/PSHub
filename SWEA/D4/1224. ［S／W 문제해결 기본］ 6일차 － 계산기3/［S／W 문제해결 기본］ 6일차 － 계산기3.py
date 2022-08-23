def postfix(word):  # 중위 -> 후위 표기식 변환 함수
    stack = []
    result = ''

    for token in word:                              # 모든 토큰 검사
        if token in '*+()':                         # 연산자 or 괄호라면
            if not stack or token == '(':           # 빈 스택 or 토큰이 (
                stack.append(token)                 # 스택에 즉시 push
            elif token == '*':                      # * 라면
                while stack and stack[-1] in '*':   # 스택의 마지막 요소가 보다 낮은 우선 순위를 갖는 토큰이 될 때까지
                    result += stack.pop()           # pop
                stack.append(token)                 # 그리고 스택에 현재 토큰 push
            elif token == '+':                      # + 라면
                while stack and stack[-1] != '(':   # 스택의 마지막 요소가 (이 나올 때까지
                    result += stack.pop()           # pop
                stack.append(token)                 # 그리고 스택에 현재 토큰 push
            elif token == ')':                      # ) 라면
                while stack and stack[-1] != '(':   # 스택의 마지막 요소가 (이 나올 때까지
                    result += stack.pop()           # pop
                stack.pop()                         # 그리고 마지막 (도 pop
        else:                                       # 피연산자라면
            result += token                         # resutl에 즉시 추가

    while stack:    # 잔고 털기~
        result += stack.pop()

    return result   # 후위 표기식 리턴


def cal(word):                       # 후위 표기식 연산 함수
    stack = []
    for char in word:
        if char not in '*+':         # 피연산자라면
            stack.append(int(char))  # 스택에 즉시 push
        else:                        # 연산자라면
            y = stack.pop()          # 피연산자 두개 pop
            x = stack.pop()
            if char == '*':          # 연산 수행 후 스택에 push
                stack.append(x * y)
            else:
                stack.append(x + y)

    return stack[-1]    # 스택엔 연산 결과가 하나 남아 있게 됨


for tc in range(1, 11):
    n = int(input())
    print(f'#{tc} {cal(postfix(input()))}')
