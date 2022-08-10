# 프로그래머스_레벨 2_2 N 타일링
# 220810

def solution(n):
    answer = [0, 1, 2]
    
    while len(answer) <= n:
        answer.append((answer[-1] + answer[-2]) % 1000000007)
    
    return answer[n]