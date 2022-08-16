t = int(input())
for tc in range(1, t + 1):
    # 단어 2차원 리스트의 값을 각각 빈 문자열로 초기화
    # 행 길이 5, 열 길이 15
    words = [[''] * 15 for _ in range(5)]

    for i in range(5): # 5줄의 단어 입력
        word = input()
        for j in range(len(word)): # words의 각 행 리스트 수정
            words[i][j] = word[j]

    print(f'#{tc}', end=' ')
    # 글자들을 세로로 읽어 출력
    for j in range(15):
        for i in range(5):
            print(words[i][j], end='')
    print()