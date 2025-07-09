import sys

nums = list(map(int, sys.stdin.readline().split()))[:9]
print(f"{max(nums)}\n{nums.index(max(nums)) + 1}")
