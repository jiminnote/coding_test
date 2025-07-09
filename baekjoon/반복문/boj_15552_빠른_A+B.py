import sys

N = int(sys.stdin.readline())
result = []

for i in range(N):
    A,B = map(int,sys.stdin.readline().split())
    result.append(A+B)

sys.stdout.write('\n'.join(map(str, result)) + '\n')