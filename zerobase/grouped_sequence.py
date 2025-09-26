# 다음 수열을 보고 수열의 합이 최초 100을 초과하는 n번째 항의 값과 n을 출력하는 프로그램을 만들어보자.


total, n,k= 0,0,2

flag = True
while flag:
    for i in range(1, k):         
        num = i               
        term = num / (k-i)
        n += 1
        total += term

        if total > 100:   
            print(f"n = {n}, 항 값 = {term}")
            flag = False
            break
    k += 1

print(f'{n}항: {round(total,2)}')