for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    binary_num = format(m, 'b')     # 정수 m을 2진수로 변환
    if len(binary_num) < n:         # n이 변환한 2진수의 길이보다 큰 경우 0 붙여주기
        binary_num = '0' * (n - len(binary_num)) + binary_num

    result = ''
    for bit in binary_num[-n:]:     # 2진수의 마지막 n개의 비트 확인
        if bit == '0':              # 꺼져 있는 비트가 있다면
            result = 'OFF'          # 결과값을 OFF으로!
            break                   # 브렉끼
        result = 'ON'               # 0인 경우가 한번도 없다면 모두 켜져 있다!

    print(f'#{tc} {result}')