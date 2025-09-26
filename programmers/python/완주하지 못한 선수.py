# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import Counter

def solution(participant, completion):
    count_p = Counter(participant)
    count_c = Counter(completion)
    diff = count_p - count_c
    return list(diff.keys())[0]