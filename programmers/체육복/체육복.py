# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    
    a=set(reserve)-set(lost) # 체육복 두 벌 있던 학생들  중 잃어버린 학생이 있으면 제거(체육복 두 벌이었다가 한 벌 된 학생들을 여벌옷 있는 학생목록에서 제거)
    b=set(lost)-set(reserve) # 잃어버리긴 했지만 여벌있는 상태에서 잃어버렸으니 자기꺼는 있다! 체육복없는 학생목록에서는 제거
  
    for i in a: #여벌이 있는 학생들 한명한명 확인하기
        if i-1 in b: #잃어버린 학생 중 여벌이 있는 학생 바로 앞번호이면
            b.remove(i-1)  #옷 빌리고 잃어버린 학생목록에서 제거
        elif i+1 in b: # 여벌이 있는 학생 바로 뒷번호면
            b.remove(i+1) #옷 빌리고 잃어버린 학생목록에서 제거
            
    return n - len(b) # 전체 학생 수에서 옷 못빌린 학생수(인덱스 길이) 빼기
    
    
print(solution(5,[2,4],[1,3,5]))