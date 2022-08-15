# 프로그래머스_레벨 2_숫자 블록
# 220815
# 문제 해결 포인트
# 각 숫자의 자신이 아닌 가장 큰 약수를 구해야 겠다!
# 시간 효율을 생각해야 한다..
# 그리고 왜 효율성 테스트에서 걸리는지... 문제를 잘 읽어보기

import math

def solution(begin, end):
    ans = [1] * (end - begin + 1)
    nums = list(range(begin, end+1))
    
    for i in range(2, int(math.sqrt(end)+1)):
        for idx, val in enumerate(nums):
            if val % i == 0:
                if val // i > 10000000: continue
                else: ans[idx] = max(val//i, ans[idx])
                
    for i in range(len(nums)):
        if nums[i] == 1: ans[i] = 0
                
    return ans