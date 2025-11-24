"""
문제: 공 넣기 (BOJ 10810)
설명:
  - 바구니 N개, 공 번호는 명령마다 i~j 범위에 k번 공을 넣는다.
  - 모든 명령을 수행한 뒤 바구니 배열을 출력한다.
시간복잡도: O(N + M)
"""

import sys

N,M = map(int,sys.stdin.readline().split())
baskets=[0]* N

for _ in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    baskets[i-1:j] = [k] * (j - i+1)

print(*baskets)


