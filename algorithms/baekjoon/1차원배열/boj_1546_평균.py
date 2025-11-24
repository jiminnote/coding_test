"""
문제: 평균 (BOJ 1546)
출처: 백준

설명:
  - 최고점 기준으로 점수를 조정 후 평균 계산
"""

import sys
import statistics

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
sorted_score = sorted(score, reverse=True)


list = [ sorted_score[i] / sorted_score[0] * 100 for i in range(len(sorted_score))]


print(statistics.mean(list))

