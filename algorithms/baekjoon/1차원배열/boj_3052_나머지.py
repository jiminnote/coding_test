
"""
문제: 나머지 (BOJ 3052)
설명:
  - 총 10개의 정수를 입력받아 각각 42로 나눈 나머지를 구함
  - 서로 다른 나머지가 몇 개 존재하는지 출력
시간복잡도: O(10) = O(1)
"""

nums = []
divide =  []

for _ in range(10):
    n = int(input())
    divide.append(n%42)
print(len(list(set(divide))))
  # 확인용 출력
