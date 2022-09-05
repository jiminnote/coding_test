def solution(lottos, win_nums):
    a=[]

    #당첨된 숫자들 분리
    for i in lottos:
        if i in win_nums:
            a.append(i) 

    #당천된 숫자들로 순위확인
    if len(a) >1:      
        result = 7-len(a) 
    else:
        result = 6

    #최고순위 확인하기   
    first = result-lottos.count(0)
    
    if first == 0:
        first=1
    return [first,result]
