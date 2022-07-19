# 프로그래머스_레벨 2_가장 큰 수
# 220719

def solution(numbers):
    numbers_str = []
    answer = ''
    for number in numbers: numbers_str.append(str(number))
    numbers_str.sort(key=lambda x: x*3)
    
    while numbers_str: answer += numbers_str.pop()
    
    return str(int(answer))