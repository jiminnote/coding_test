# 박스에 ‘꽝’이 적힌 종이가 6장 있고, ‘선물’이 적힌 종이가 4장이 있을 때,
# 파이썬을 이용해서 ‘꽝’3장과 ‘선물’ 3장을 뽑는 확률(%)을 출력하자

def comb_func(n, r):
    perm, fact_r = 1, 1
    for i in range(n, n - r, -1):   #
        perm *= i
    for i in range(r, 0, -1):       
        fact_r *= i
    return perm // fact_r  

sample = comb_func(10, 6)   
event1 = comb_func(6, 3)    
event2 = comb_func(4, 3)     

pro = (event1 * event2) / sample
print(f"확률 =({pro*100:.2f}%)")