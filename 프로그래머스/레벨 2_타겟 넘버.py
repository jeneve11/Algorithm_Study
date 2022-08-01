# 프로그래머스_레벨 2_타겟 넘버
# 220801

from itertools import combinations

def solution(numbers, target):  
    answer = 0
    lists = []
    sum_numbers = sum(numbers)
    
    # lists에 가능한 조합 경우를 모두 추출
    for i in range(len(numbers)):
        lists.append(list(combinations(numbers, i)))
        
    # lists의 모든 조합 경우 중 target을 만들 수 있는 경우를 모두 탐색하여
    # 가능한 경우 발견할 때 마다 answer += 1
    for i in lists:
        for j in i:
            if sum_numbers - (2*sum(j)) == target: answer += 1
    return answer