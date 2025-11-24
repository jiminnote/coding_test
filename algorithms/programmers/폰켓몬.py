# https://school.programmers.co.kr/learn/courses/30/lessons/1845
from collections import Counter
def solution(nums):
    n = int(len(nums)//2)
    species_count = len(set(nums))
    return min(n, species_count)