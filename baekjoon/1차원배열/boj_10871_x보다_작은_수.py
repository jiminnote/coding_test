import sys

N,X = map(int,sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))[:N]

# arr = []
# for i in range(N):
#     if nums[i] < X:
#         arr.append(nums[i])

# print(*arr)


print(*[num for num in nums if num < X])