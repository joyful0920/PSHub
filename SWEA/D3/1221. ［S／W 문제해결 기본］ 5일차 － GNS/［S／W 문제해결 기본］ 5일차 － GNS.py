nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())
for _ in range(t):
    tc, n = input().split()
    string_nums = list(input().split())

    int_nums = sorted([nums.index(num) for num in string_nums])

    print(f'{tc}')
    for idx in int_nums:
        print(nums[idx], end=' ')