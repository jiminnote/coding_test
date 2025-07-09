import sys

N,M = map(int,sys.stdin.readline().split())
baskets=[0]* N

for _ in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    baskets[i-1:j] = [k] * (j - i+1)

print(*baskets)


