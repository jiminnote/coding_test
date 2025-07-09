# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    a,b=0,0
    for i in sizes:
        i.sort() #입력받은 모든 명함의 리스트를 [작은 수, 큰 수] 로 정렬
        a=max(a,i[0]) #size[i][0] 중 가장 큰수
        b=max(b,i[1]) #size[i][1] 중 가장 큰수
    return a*b 