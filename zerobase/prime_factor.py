# 100부터 1000사이의 난수를 소인수분해를 하고 각각의 소인수에 대한 지수를 출력하는 프로그램을 만들어보자.

import random

# 난수 생성
a = random.randint(100, 1000)
print(f"난수: {a}")

# 소인수와 지수 저장
prime_factors = {}
num = a
prime = 2
while prime <= num:
    if num % prime == 0:
        prime_factors[prime] = prime_factors.get(prime, 0) + 1
        num //= prime
    else:
        prime += 1

# 출력
for factor, exponent in prime_factors.items():
    print(f"{factor}의 지수 : {exponent}")
