import random

# 난수 생성
a = random.randint(100, 1000)

# 약수
divisors = []
for i in range(1, a + 1):
    if a % i == 0:
        divisors.append(i)

# 소수 (약수 중 소수만 추출)
prime_numbers = []
for d in divisors:
    if d > 1:  # 1은 소수가 아님
        is_prime = True
        for j in range(2, d):
            if d % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(d)

# 소인수 (소수이면서 a를 나누는 수)
prime_factors = []
num = a
prime = 2
while prime <= num:
    if num % prime == 0:
        prime_factors.append(prime)
        num //= prime
    else:
        prime += 1

print(f'{a}의 약수: {divisors}')
print(f'{a}의 소수: {prime_numbers}')
print(f'{a}의 소인수: {prime_factors}')