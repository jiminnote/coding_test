"""
문제: 최댓값 (BOJ 2562)
설명:
  - 총 9개의 자연수가 한 줄씩 입력됨
  - 최댓값과 그 값의 입력 순서를 출력
"""
import sys

nums = list(map(int, sys.stdin.readline().split()))[:9]
print(f"{max(nums)}\n{nums.index(max(nums)) + 1}")
