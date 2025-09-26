num = int(input())

result = 1
for n in range(1, num+1):
  result *= n
print(f'{num}!:{result}')