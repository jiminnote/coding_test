# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer=len(s )
    for n in range(1,len(s)//2+1):
        result=''
        cnt=1
        tmp=s[:n] #단위문자열 초기화

        for i in range(n,len(s)+n,n):
            if tmp == s[i:i+n]: #이전 문자열과 같다면
                cnt+=1
            else: #이전 문자열과 다르다면
                if cnt==1: #카운트가 1이면 문자열 그대로 저장
                    result+=tmp
                else: #카운트가 2 이상이면
                    result+=str(cnt)+tmp #카운트포함하여 문자열 저장
                tmp=s[i:i+n]
                cnt=1
        answer=min(answer,len(result))
    return answer
