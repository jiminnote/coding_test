# import sys 

# N = int(sys.stdin.readline())
# A_nums = []
# B_nums = []
# result = []

# for i in range(N):
#     A,B = map(int,sys.stdin.readline().split())
#     A_nums.append(A)
#     B_nums.append(B)
#     result.append(A+B)

# for i in range(N):
#     sys.stdout.write(f'Case #{i + 1}: {A_nums[i]} + {B_nums[i]} = {result[i]}\n')

# GPT
import sys 

N = int(sys.stdin.readline())
outputs = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    outputs.append(f'Case #{i + 1}: {A} + {B} = {A + B}')

sys.stdout.write('\n'.join(outputs) + '\n')