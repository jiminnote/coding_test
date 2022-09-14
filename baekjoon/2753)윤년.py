# https://www.acmicpc.net/problem/2753

a = int(input()) #연도 입력

if a%4 == 0 and a%100 != 0: # 4의 배수 and 100의 배수가 아닐 때
   print('1') #윤년
            
elif a%400 == 0: #400의 배수
   print('1') #윤년
         
else : #그 외의 경우의 수
  print('0') #윤년X