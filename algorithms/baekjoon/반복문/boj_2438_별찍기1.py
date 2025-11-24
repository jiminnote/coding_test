
import sys 

N = int(sys.stdin.readline())
stars = []

for i in range(N):
    stars.append('*'*(i+1))

sys.stdout.write('\n'.join(stars) + '\n')
