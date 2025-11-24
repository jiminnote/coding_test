# n, m, k 공백을 기준으로 구분하여 입력 받기
n,m,k = map(int,input().split()) 
# N개의 수를 공백을 기준으로 구분하여 입력 받은 후 정렬
b=sorted(list(map(int,input().split())))

result = 0
print(b)
for i in range(m): 
  for i in range(k):
    result += b[-1] # k번 반복문이 도는 동안 가장 큰 수 계속 덧셈
    m-=1   # 한번 더할 때 마다 m-1
    if m==0: #k번 돌기 전에 m=0이 되면 break
      break
  result += b[-2] # 위에서 뺼셈이 이루어지고 남은 m두 번째로 큰 수
  m-=1
  if m==0:
      break
print(result)