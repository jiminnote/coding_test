# 100부터 1000사이의 2개의 난수에 대해서 공약수와 최대공약수를 출력하고,
# 서로소인지 출력하는 프로그램을 만들어보자.

import random

# 난수 생성
a, b = random.randint(100, 1000), random.randint(100, 1000)

common_divisors = []
gcd = 1 


for i in range(1, min(a, b) + 1):  # min(a,b)까지만 확인해도 충분
    if a % i == 0 and b % i == 0:
        common_divisors.append(i)
        gcd = i 

print(f'{a}와 {b}의 공약수: {common_divisors}')
print(f'{a}와 {b}의 최대공약수: {gcd}')

# 서로소 여부 출력
if gcd == 1:
    print(f'{a}와 {b}는 서로소입니다')
else:
    print(f'{a}와 {b}는 서로소가 아닙니다')