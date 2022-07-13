# 프로그래머스_레벨 1_소수 만들기
# 220713

import itertools, math

def solution(nums):
    answer = 0
    
    it = list(itertools.combinations(nums, 3))
    for i in it:
        if isPrime(sum(i)): answer += 1
        
    return answer

def isPrime(num):
    for i in range(2, math.ceil(num ** 1/2)): 
        if num % i == 0:
            return False
        
    return True