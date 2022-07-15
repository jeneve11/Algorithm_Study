# 프로그래머스_레벨 1_나머지가 1이 되는 수 찾기
# 220715

def solution(n):
    for i in range(1, n):
        if n%i == 1:
            return i
    return -1