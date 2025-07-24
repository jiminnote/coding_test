def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_nums = sorted(numbers, key=lambda x: x*10, reverse=True)
    result = ''.join(sorted_nums)
    if sorted_nums[0] == '0':  ## 이부분 추가!
        return '0'
    return result
