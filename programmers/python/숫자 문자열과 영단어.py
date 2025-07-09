# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = s 
    num_dict ={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    
    for i in num_dict.items():
        answer = answer.replace(i[1], str(i[0]))   


    return int(answer)