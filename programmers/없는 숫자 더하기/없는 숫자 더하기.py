def solution(numbers):
    result = [1,2,3,4,5,6,7,8,9,0]
    arr = []
    for i in result:
        if i not in numbers:
            arr.append(i)
    return sum(arr)