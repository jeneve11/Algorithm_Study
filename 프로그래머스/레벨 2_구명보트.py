# 프로그래머스_레벨 2_구명보트
# 220807

# n log n 이하로 돌려야함
from collections import deque

def solution(people, limit):
    answer = []
    
    people.sort()
    people = deque(people)
    print(people)

    while True:
        right = people.pop()
        while True:
            if not people: return len(answer) + 1
            left = people[0]
            if left + right > limit:
                answer.append(right)
                break
            else: right += people.popleft()