import sys

N,K = map(int,sys.stdin.readline().split())

person= [i+1 for i in range(N)]
people = []
josephus = 0

while person:
    josephus = (josephus + K - 1) % len(person)  # 원형 순회
    people.append(person.pop(josephus))

print(people)



import sys

N,K = map(int,sys.stdin.readline().split())

person= [i+1 for i in range(N)]
people = []
josephus = 0

while person:
    josephus = (josephus + K - 1) % len(person)  # 원형 순회
    people.append(person.pop(josephus))

print("<" + ", ".join(map(str, people)) + ">")

















