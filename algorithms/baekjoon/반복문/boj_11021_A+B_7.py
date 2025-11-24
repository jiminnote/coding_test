import sys 

N = int(sys.stdin.readline())
result = []

for i in range(N):
    A,B = map(int,sys.stdin.readline().split())
    result.append(A+B)

for i in range(N):
    sys.stdout.write('Case #'+int(i)+':'+result[i])
     #GPT :  sys.stdout.write(f'Case #{i + 1}: {result[i]}\n')