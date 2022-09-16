# https://www.acmicpc.net/problem/2884

h,m = map(int,input().split()) # h 입력 후 띄어쓰기하고 m 입력

result_h,result_m = h,m
  


if 45 <= m <= 59:  #45분~59분은 -45해도 h변함없음
   result_m -= 45
elif 0 <= m <= 44:  #44분~0분은 -45하면 h가 변함
   a= m-45
   result_m=60+a      #m -45 하고 나온 음수의 값에 60을 더해서 저장
  
   if result_h == 0:  #0시에서 -1을 할 경 23이 되야되기때문에
    result_h = 24     #0 입력시 24로 변경하여 저장하기
   result_h-= 1       #m이 0~44일경우 45분을 빼려면 h-1 되어야함
  
  
   

print(abs(result_h) ,abs(result_m)) 
#시계는 양수값만 보여지기때문에 abs()함수적용
#사실 없어도 문제는 맞지만 그냥 한번 써봤음