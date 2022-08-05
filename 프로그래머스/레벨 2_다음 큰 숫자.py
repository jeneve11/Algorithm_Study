# 프로그래머스_레벨 2_다음 큰 숫자
# 220805

def solution(n):
    # n의 1 갯수 계산
    one_cnt = sum([int(i) for i in list(bin(n)) if i == '1'])
    temp = n+1

    while True:
        # temp의 1 갯수와 n의 1 갯수 비교
        if sum([int(i) for i in list(bin(temp)) if i == '1']) == one_cnt: break
        else: temp += 1
    
    return temp

