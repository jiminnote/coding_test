# 100부터 1000사이의 2개의 난수에 대해서 최대공약수와 최소공배수를 출력하는
# 프로그램을 만들어보자.

import random

# 난수 생성
a, b = random.randint(100, 1000), random.randint(100, 1000)

# 최대공약수
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# 최소공배수
lcm = (a * b) // gcd

print(f'{a}와 {b}의 최대공약수: {gcd}')
print(f'{a}와 {b}의 최소공배수: {lcm}')