def factorial_func(n):
    if n == 1:      
        return 1
    return n * factorial_func(n - 1) 
num = int(input())
print(f'{num}! = {factorial_func(num)}')