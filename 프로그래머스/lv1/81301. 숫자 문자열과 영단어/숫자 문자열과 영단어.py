def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    while len(s) > 0:
        if s[0].isnumeric():
            answer += s[0]
            s = s[1:]
        else:
            if s[:5] in nums:
                answer += str(nums.index(s[:5]))
                s = s[5:]
            elif s[:4] in nums:
                answer += str(nums.index(s[:4]))
                s = s[4:]
            else:
                answer += str(nums.index(s[:3]))
                s = s[3:]

    return int(answer)