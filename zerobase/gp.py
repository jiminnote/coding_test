# 다음 수열의 일반항을 구하고 n번째항의 값과 합을 구하는 프로그램을 만들어보자.
# 입력: a1(첫항), r(공비), n(몇 번째 항까지)

a1, r, n = map(int, input().split())
term = a1
sn = a1

nth = a1 * (r ** (n - 1))
print(f"{n}번째 항(공식): {nth}")

sn_formula = a1*(1 - r**n)/(1-r)
print(f"{n}번째 항(공식): {int(sn_formula)}")