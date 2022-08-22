def post(word):  # 중위 -> 후위 표기 변환 함수
    stack = []
    result = ''

    for token in word:  # 각각의 토큰 검사
        if token in '*/+-':                          # 연산자라면
            if not stack:                            # 스택이 빈 상태라면
                stack.append(token)                  # 스택에 추가
            elif token in '*/':                      # */ 연산자라면
                while stack and stack[-1] in '*/':   # 보다 우선순위가 낮은 연산자 +-를 만날때까지
                    result += stack.pop()            # 스택에서 pop한 값을 result에 추가
                stack.append(token)
            else:                                    # +- 연산자라면
                while stack:                         # 먼저 스택에 들어온 연산자들을
                    result += stack.pop()            # 스택에서 모두 pop해 result에 추가
                stack.append(token)
        else:                                        # 피연산자면
            result += token                          # 바로 result에 추가

    while stack:    # 잔고 털기~
        result += stack.pop()

    return result   # 후위 표기식 리턴


def cal(word):  # 후위 표기 수식 계산 함수
    stack = []
    for char in word:                # 수식 검사
        if char not in '*/+-':       # 피연산자면
            stack.append(int(char))  # 스택에 추가
        else:                        # 연산자면
            a = stack.pop()          # 스택에에서 피연산자 두개 pop
            b = stack.pop()
            if char == '+':          # 뒤에 오는 피연산자가 먼저 뽑히니
                stack.append(b + a)  # 계산은 뽑힌 역순으로 해줘야 원래 형태 대로 됨!
            elif char == '-':
                stack.append(b - a)
            elif char == '*':
                stack.append(b * a)
            else:
                stack.append(b / a)

    return stack[-1]  # 저장된 게산 결과 반환


for tc in range(1, 11):
    n = int(input())        
    postfix = post(input())     # 중위 -> 후위 표기법
    print(f'#{tc} {cal(postfix)}')         # 후위 표기 수식을 계산해 출력
