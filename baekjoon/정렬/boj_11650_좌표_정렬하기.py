import sys

N = int(sys.stdin.readline())

points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

for x,y in sorted(points):
    print(x, y)
