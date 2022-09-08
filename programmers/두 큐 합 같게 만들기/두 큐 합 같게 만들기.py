# https://school.programmers.co.kr/learn/courses/30/lessons/118667
def solution(queue1, queue2):
    cnt = 0
    
    if (sum(queue1)+sum(queue2))%2:
        return -1
    for i in range(300001):
        if sum(queue1) == sum(queue2):
             break
        elif sum(queue1) < sum(queue2):
            queue1.append(queue2.pop(0))
            cnt += 1
        else:
            queue2.append(queue1.pop(0))
            cnt += 1
            
    return cnt
 