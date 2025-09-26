# 파이썬을 이용해서 다음 조합들의 값을 구하는 프로그램을 만들어 보자.
# 1. 9C4
# 2. 6C2

def nCrfunc(N,r):
    perm, fact_r, comb = 1, 1, 1      

# 순열 (NPr)
    for i in range(N, (N - r), -1):
        perm *= i

# r! (팩토리얼)
    for i in range(r, 0, -1):
      fact_r *= i

# 조합 (nCr = nPr / r!)
    comb = int(perm / fact_r)

    return f'{N}C{r}: {comb}'

print(nCrfunc(9,4))
print(nCrfunc(6,2))