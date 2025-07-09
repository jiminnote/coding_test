# import sys  # 표준 입력을 더 빠르게 받기 위해 sys 모듈 사용

# N = int(sys.stdin.readline())  # 첫 줄에서 정수 N 입력받음 (출력할 줄 수)

# # N x N 배열을 '*'로 초기화
# stars = [['*' for _ in range(N)] for _ in range(N)]

# # 각 줄에서 별 앞부분을 공백으로 바꿔서 오른쪽 정렬된 삼각형 모양으로 만듦
# for i in range(N):
#     for j in range(N - i - 1):
#         stars[i][j] = ' '  # i번째 줄 앞의 j번째 열을 공백으로 변경

# # 각 줄을 문자열로 합쳐 출력
# for row in stars:
#     print(''.join(row))  # 리스트를 문자열로 합쳐 출력

import sys  # 표준 입력을 더 빠르게 받기 위해 sys 모듈 사용

N = int(sys.stdin.readline())  # 첫 줄에서 정수 N 입력받음 (출력할 줄 수)

for i in range(1,N+1):
    sys.stdout.write(' '*(N-i)+'*'*i + '\n')
