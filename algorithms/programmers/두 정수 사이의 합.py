# https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    n=[]
    if a<b:
     for i in range(b-a+1):
      n.append(a+i)
    elif a>b:
     for i in range(a-b+1):
      n.append(b+i)
    else:
      n.append(a)

    return sum(n)