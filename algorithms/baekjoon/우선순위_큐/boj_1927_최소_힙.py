import sys, heapq

N = int(sys.stdin.readline())
points = []
count = 0

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        count += 1
        if points:
            print(heapq.heappop(points))
        else:
            print(0)
    else:
        heapq.heappush(points, x) 











