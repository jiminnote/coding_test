from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    print(queue)

    while queue:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer