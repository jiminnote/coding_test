# https://www.acmicpc.net/problem/4344

C=int(input())  #테스트케이스의 수 입력


for i in range(C):  #테스트케이스의 수만큼 반복
 n = list(map(int, input().split())) #공백으로 입력받기
 b=[] #평균값을 넘는 점수 저장할 배열선언
 for j in range(1,len(n)): #입력받은 점수개수 만큼 반복(0부터 반복하면 학생수를 쓴 n[0]도 돌아가니까 1부터!)
   if n[j] > sum(n[1:])/int(n[0]): #n[1:j] 점수 중 평균값을 넘을때
    b.append(n[j]) #평균값넘으면 배열b에 넣기
  
 if len(b)>0: #배열 b가 0보다 클때
  print('{:.3f}'.format(round((100/((len(n)-1)/len(b))), 4))+"%") #
 else: #배열 b가 0이거나 0보다 작으면
  print('0.000%')