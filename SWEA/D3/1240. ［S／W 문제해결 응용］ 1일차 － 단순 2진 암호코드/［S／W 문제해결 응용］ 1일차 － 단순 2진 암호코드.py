patterns = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

for c in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    codes = ''
    breaker = False
    for i in range(n):
        for j in range(m - 1, -1, -1):          # 코드의 각 행을 뒤에서부터 확인
            if arr[i][j] == '1':                # 1인 지점이라면
                codes = arr[i][j - 55:j + 1]    # 해당 열을 기준으로 앞으로 56열의 문자열을 최종 확인 코드로!
                breaker = True
                break
        if breaker:
            break

    total = 0
    result = 0
    temp = 0
    for i in range(0, 57, 7):           # 코드를 6자리씩 끊어서 확인
        number = codes[i:i + 7]
        for j in range(10):             
            if number == patterns[j]:   # 일치하는 패턴이 있으면
                result += j             # 결과 변수에 해당 패턴의 숫자 더해주고
                temp += 1               # 홀짝 판단 확인 변수 temp + 1
                if temp % 2 == 1:       # 홀수 자리라면
                    total += j * 3      # total에 3을 곱해서 더해주고
                else:                   # 아니면
                    total += j          # 걍 더해주고..
                break

    if total % 10 == 0:             # total을 10으로 나눴을 때 0인 경우만 올바른 암호코드
        print(f'#{c} {result}')
    else:
        print(f'#{c} 0')