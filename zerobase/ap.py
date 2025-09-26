# 다음 수열의 일반항을 구하고 n번째항의 값과 합을 구하는 프로그램
n = int(input())
start, step = 4,6   

# n번째 항 
numth = start+(n-1)*step  
# 합 
sum_n = n * (start + numth) / 2  

print(numth, int(sum_n))