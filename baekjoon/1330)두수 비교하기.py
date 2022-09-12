# https://www.acmicpc.net/problem/1330

a,b = map(int,input().split()) #첫 줄에서 a,b 공백 한칸으로 구분하여 입력받음
 
if a>b:
      print('>')
            
elif a<b:
      print('<')
         
elif a==b:
      print('==')