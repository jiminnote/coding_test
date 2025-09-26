# 파이썬을 이용해서 다음 순열들의 값을 구하는 프로그램을 만들어 보자
# 1. 9P4
# 2. 6P2

def perfunc(n, r):
    result = 1
    print(f'---{n}P{r}---')
    for i in range(n, n - r, -1):
        print(f'{i}')
        result *= i
    return result

a = perfunc(9, 4)
b = perfunc(6, 2)
print('------')
print(f'1. 9P4 = {a}')
print(f'2. 6P2 = {b}')