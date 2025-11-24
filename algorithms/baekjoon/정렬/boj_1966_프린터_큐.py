import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    doc, order = map(int, sys.stdin.readline().split())  # 문서 수, 문서위치
    priorities = list(map(int, sys.stdin.readline().split()))  # 각 문서의 우선순위

    queue = deque((i, p) for i, p in enumerate(priorities))  # (문서번호, 중요도)
    count = 0 # 인쇄 순서 카운트

    while queue: # 큐가 빌때까지 반복
        current = queue.popleft() # 가장 앞의 문서를 꺼냄

        # 뒤에 더 높은 우선순위가 하나라도 있다면 다시 뒤로 보냄
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count += 1  # 문서를 인쇄함
            if current[0] == order:
                print(count)
                break