def sudoku(array):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            if cnt[array[i][j]] == 0:
                cnt[array[i][j]] = 1
            else:
                return False
    
    for j in range(9):
        cnt = [0] * 10
        for i in range(9):
            if cnt[array[i][j]] == 0:
                cnt[array[i][j]] = 1
            else:
                return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 10
            for x in range(3):
                for y in range(3):
                    if cnt[array[x][y]] == 0:
                        cnt[array[x][y]] = 1
                    else:
                        return False
    
    return True
                    
t = int(input())
for test in range(1, t + 1):
    array = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(array)

    print(f"#{test} ", end='')
    if result:
        print(1)
    else:
        print(0)