import sys, heapq

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if points:
            print(heapq.heappop(points)[1])
        else:
            print(0)
    else:
        heapq.heappush(points, (abs(x), x))









