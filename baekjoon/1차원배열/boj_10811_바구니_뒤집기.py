#
# # 1차 시도 실패
# import sys
#
# N,M = map(int,sys.stdin.readline().split())
# N_list = [n+1 for n in range(N)]
#
# for _ in range(M):
#     i,j = map(int,sys.stdin.readline().split())
#     N_list[i-1:j] = list(reversed(N_list[i-1:j]))
#
# print(N_list)


# 2차 시도

import sys

N,M = map(int,sys.stdin.readline().split())
N_list = [n+1 for n in range(N)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    N_list[i-1:j] = list(reversed(N_list[i-1:j]))

print(*N_list)

