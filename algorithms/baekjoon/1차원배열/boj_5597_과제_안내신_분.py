"""
문제: 과제 안 내신 분..? (BOJ 5597)
설명:
  - 1부터 30까지 학생 번호 중,
    제출한 28명의 번호가 입력됨
  - 제출하지 않은 2명의 번호를 찾아
    오름차순으로 출력
시간복잡도: O(30) = O(1)
"""

import sys
submitted_students = [int(sys.stdin.readline()) for _ in range(28)]
missing = sorted(set(range(1, 31)) - set(submitted_students))
for student in missing:
    print(student)

