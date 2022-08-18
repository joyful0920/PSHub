for tc in range(1, 11):
    length, s = input().split()

    result = []                 # 비밀번호 리스트
    for n in s:                 # 비밀번호 숫자 하나씩 확인
        if not result:          # 비밀번호 리스트가 비어있다면
            result.append(n)    # 현재 숫자 n 추가
        elif result[-1] == n:   # 현재 n이 직전 추가 숫자와 같다면
            result.pop()        # 직전 숫자 삭제
        else:                   # 그 외의 경우
            result.append(n)    # 현재 숫자 n 추가

    print(f'#{tc} ', end='')
    for n in result:
        print(n, end='')
    print()