# 프로그래머스_레벨 2_이진 변환 반복하기
# 220809

ans = [0, 0]

def change(num):
    one_cnt = num.count('1')
    
    ans[0] += 1
    ans[1] += len(num) - one_cnt
    
    return str(bin(one_cnt))[2:]

def solution(s):
    while s != '1': s = change(s)
    return ans