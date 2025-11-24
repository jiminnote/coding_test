import sys

N,M = map(int,sys.stdin.readline().split())

baskets = [i + 1 for i in range(N)]

# baskets=[]
# for i in range(N):
#     baskets.append(i+1)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    a,b = baskets[i-1],baskets[j-1]
    baskets[i-1],baskets[j-1] = b,a

print(*baskets)


