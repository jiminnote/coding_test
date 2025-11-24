import sys

N = int(sys.stdin.readline())
result = []
for _ in range(N):
   M = int(sys.stdin.readline())
   result.append(M)

for j in sorted(result):
    print(j)