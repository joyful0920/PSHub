from copy import deepcopy

for tc in range(1, int(input()) + 1):
    b = list(map(str, input()))     # 2진수
    t = list(map(str, input()))     # 3진수

    binary_nums = []                # 1자리만 바꿔서 가능한 2진수 리스트
    for i in range(1, len(b)):      # 주어진 2진수의 둘째 자리부터 확인
        temp = deepcopy(b)
        if b[i] == '0':             # 0이면
            temp[i] = '1'           # 해당 자리의 숫자를 1로 바꾸고
        else:                       # 1이면
            temp[i] = '0'           # 2로 바꾸고
        binary_nums.append(int(''.join(temp), 2))   # 1자리만 바꿔준 2진수를 10진수로 바꿔서 리스트에 추가

    trinary_nums = []               # 1자리만 바꿔서 가능한 3진수 리스트
    for i in range(len(t)):
        if i == 0:                  # 첫째 자리에 대한 처리
            temp = deepcopy(t)
            if t[i] == '1':         # 1이면 2로 바꿔 보고
                temp[i] = '2'
            else:                   # 2면 1로 바꿔 보고
                temp[i] = '1'
            trinary_nums.append(int(''.join(temp), 3))      # 첫째 자리만 바꿨을 때 가능한 3진수를 10진수로 바꿔 리스트에 추가
        else:                                               # 둘째 자리부터는
            temp1, temp2 = deepcopy(t), deepcopy(t)         # 바꿀 수 있는 경우의 수가 2개!
            if t[i] == '0':
                temp1[i], temp2[i] = '1', '2'
            elif t[i] == '1':
                temp1[i], temp2[i] = '0', '2'
            else:
                temp1[i], temp2[i] = '0', '1'
            trinary_nums.append(int(''.join(temp1), 3))     # 1자리만 바꿨을 때 가능한 3진수의 경우들을 10진수로 변환하여 각각 리스트에 추가
            trinary_nums.append(int(''.join(temp2), 3))

    result = list(set(binary_nums) & set(trinary_nums))     # 두 집합의 교집합을 구하면 추측 가능한 숫자 하나를 얻을 수 있다.
    print(f'#{tc} {result[0]}')