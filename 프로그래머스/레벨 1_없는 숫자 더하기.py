# 프로그래머스_레벨 1_없는 숫자 더하기
# 220715

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer