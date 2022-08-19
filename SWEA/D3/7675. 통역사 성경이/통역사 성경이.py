t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    words = list(map(str, input().split()))     # 입력을 공백으로 구분하여 단어 리스트 생성

    cnts = []
    cnt = 0
    for word in words:                          # 모든 단어 검사
        name = True                             # 일단 name은 True
        if word[0].isupper():                   # 단어의 첫 글자가 대문자라면
            for c in word[1:-1]:                # 맨 앞뒤를 제외한 단어의 글자 검사
                if not c.islower():             # 소문자가 아닌 경우가 있다면
                    name = False                # 이름은 아님!
                    break                       # 브렉끼
            if name:                            # 아직도 name이 True라면
                if len(word) == 1:              # 한 글자 단어 예외 처리
                    cnt += 1
                elif word[-1].islower() or word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
                    cnt += 1                    # 맨 뒷 글자를 검사해서 조건에 부합하면 cnt + 1
                                                # 문장의 끝이라면
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            cnts.append(cnt)                    # cnts에 현재까지의 cnt 추가
            cnt = 0                             # 그리고 cnt 초기화

    print(f'#{tc}', end=' ')
    print(*cnts)
