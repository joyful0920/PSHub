patterns = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = list(set(input().rstrip() for _ in range(n)))         # 배열 정보를 한줄씩 입력 받되, 셋에 저장시켜서 중복을 제거하고 다시 리스트로 반환
                                                                # rstrip()으로 개행문자를 제거하여 런타임 에러 방지

    codes = set()                                               # 실질적으로 확일할 암호코드를 저장할 자료구조도 셋으로 선언해 중복 제거
    for i in range(len(arr)):                                   # 2차원 배열의 각각의 16진수 배열을 확인해서 
        temp = ''
        for j in range(m):              
            binary_num = format(int(arr[i][j], 16), 'b')        # 16진수 숫자 하나하나 전부 2진수로 변환
            length = len(binary_num)
            if length < 4:                                      # 4자리수 미만일 수도 있으니
                binary_num = '0' * (4 - length) + binary_num    # 그런 경우엔 필요한 만큼 0을 붙여 주고
            temp += binary_num                                  # 16진수 숫자 하나 당 4자리의 2진수를 구해 temp에 붙여주기
                                                                # 16진수 문자열 -> 2진수 문자열로 변환 완료!
        one = False                                             # 직전 확인한 숫자가 0 또는 1인지 확인할 변수
        end, cnt = 0, 0                                         # end 지점의 인덱스와, 1과 0이 몇번 반복되었는지 체크해줄 변수들
        for j in range(m * 4 - 1, -1, -1):                      # 2진수 문자열을 뒤에서부터 확인
            if not end and temp[j] == '1':                      # end가 0인데 1이 등장? => 끝 지점이잖아!!
                one = True                                      # 1 등장했으니 one은 True
                end = j                                         # 현 인덱스로 끝 지점 등록
                cnt += 1                                        # 1과 0의 등장 횟수 + 1
            elif end:                                           # 끝 지점이 등록된 상태라면
                if cnt < 32:                                    # 1, 0의 등장 횟수 확인 => 32 미만이면? 8자리 암호코드 길이 불충족!
                    if one and temp[j] == '0':                  # 직전에 1이 등장했는데, 지금 0이 등장한 경우
                        one = False                             # one은 토글링 해주고
                        cnt += 1                                # 1과 0의 등장 횟수 + 1
                    elif not one and temp[j] == '1':            # 직전에 0이 등장했는데, 지금 1이 등장한 경우
                        one = True                              # one 토글링
                        cnt += 1                                # 1과 0의 등장 횟수 + 1
                else:                                           # cnt >= 32? => 8자리 암호코드 길이 만족!
                    length = (end - j - 1) // 56 + 1            # 현 인덱스와 끝 지점의 인덱스를 활용하여 실질적인 암호코드 총 길이 계산해주기
                    codes.add(temp[end - (56 * length) + 1:end + 1])    # 계산한 길이만큼 끝지점부터 2진수 문자열을 끊어서 codes 셋에 저장
                    one = False                                 # 암호코드 하나를 뽑아 냈으면
                    end, cnt = 0, 0                             # 사용했던 변수들 다시 초기 상태로 되돌려서 다음 암호코드 뽑기 준비

    result = 0                                      # 최종 결과 변수
    for code in list(codes):                        # 암호코드들 하나씩 확인
        length = len(code)                          # 길이가 56인 코드만 있는 것은 아니니
        thickness = length // 56                    # 일단 두께 계산해주고!

        if thickness > 1:                           # 두께가 1을 초과하는 경우는
            temp = ''
            for i in range(0, length, thickness):   # 두께를 range()의 step으로 활용하여
                temp += code[i]                     # 56자리 코드로 축소
            code = temp

        temp, total = 0, 0
        for i in range(1, 9):                # 7자리씩 끊어서 8번 반복할 거야
            breaker = False
            for j in range(10):              # 암호코드 패턴과 비교
                if code[:7] == patterns[j]:  # 앞 7자리 끊은 코드와 일치한 패턴이 있다면
                    if i % 2 == 1:           # 홀수 자리라면
                        temp += j * 3        # 3을 곱해서 더해주고
                        total += j           # 결과 변수에 활용할 친구는 그냥 더해주고
                    else:                    # 짝수 자리라면
                        temp += j            # 그냥 더해주고
                        total += j
                    code = code[7:]          # 계산 끝났으면 앞 7자리 날려주고!
                    breaker = True           # 다른 패턴은 더 이상 확인할 필요 없으니
                    break                    
                if breaker:                  # breaker 변수를 활용해 반복분 탈출
                    break

        if temp % 10 == 0:      # 계산한 temp가 10으로 나누어 떨어진다면
            result += total     # 올바른 암호코드잖아! 각 자리수를 더해준 total을 result에!

    print(f'#{tc} {result}')