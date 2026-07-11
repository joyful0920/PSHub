def check(s):                   # 올바른 문자열 체킹 함수
    temp = 0
    for c in s:                 # 문자열의 문자를 하나씩 검사
        if c == ')':            # 닫는 괄호면
            temp -= 1           # temp - 1
            if temp < 0:        # temp값이 0 이하로 내려가면
                return False    # 바르지 못해!
        else:                   # 여는 괄호면
            temp += 1           # temp + 1
    return True                 # temp 값이 0 이상을 쭉 유지하면 올바른 문자열!


def change(w):                      # 변환 함수
    if w == '':                     # 빈 문자열은  
        return ''                   # 그대로 반환
    else:                           # 빈 문자열이 아니라면
        left, right = 0, 0          
        for i in range(len(w)):     # 문자열을 앞에서부터 검사
            if w[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:       # 여는 괄호와 닫는 괄호 수가 같아지면
                u = w[:i + 1]
                v = w[i + 1:]
                break               # u, v 분리
        if check(u):                # u, 너 올바르구나!
            return u + change(v)    # u + v를 재귀적으로 change한 결과 리턴
        else:                       # u, 너 올바르지 않다니..
            result = '(' + change(v) + ')'
            for c in u[1:len(u) - 1]:
                if c == '(':
                    result += ')'
                else:
                    result += '('
            return result           # ( + v를 재귀적으로 change한 결과 + ) + u의 양끝을 제거하고 뒤집은 문자열 리턴


def solution(p):
    return change(p)