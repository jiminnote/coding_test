# 1차 시도 실패
# import sys
# import statistics
#
# N = int(sys.stdin.readline())
# score = list(map(int, sys.stdin.readline().split()))
# sorted_score = sorted(score, reverse=True)
#
# for i in range(len(sorted_score)):
#     sorted_score[i] = sorted_score[i] / sorted_score[0] * 100
#
#
# print(statistics.mean(sorted_score))

#2차 시도 성공
import sys
import statistics

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
sorted_score = sorted(score, reverse=True)


list = [ sorted_score[i] / sorted_score[0] * 100 for i in range(len(sorted_score))]


print(statistics.mean(list))

