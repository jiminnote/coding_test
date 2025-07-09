

import sys 

outputs = []

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    outputs.append(str(A + B))

sys.stdout.write('\n'.join(outputs) + '\n')