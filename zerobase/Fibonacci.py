# 피보나치수열에서 n항의 값과 n항까지의 합을 출력하는 프로그램을 만들어보자.
# {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …}

n = int(input())
prev2, prev1 = 0, 1   # 시작을 (0, 1)로 지정하여 루프 단순화
current = 0
total = 0
for k in range(1, n + 1):
    if k == 1:
        current = 1
    else:
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    total += current
print(f'{n}번째 항의 값: {current}')
print(f'{n}번째 항까지의 합: {total}')