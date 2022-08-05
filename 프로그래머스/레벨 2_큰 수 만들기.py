# 프로그래머스_레벨 2_큰 수 만들기
# 220804

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def func(index_dict, number, low, high):
    if high == len(number): return ''
    
    for num in range(9, -1, -1):
        temp_list = [i for i in index_dict[str(num)] if low < i <= high]
        if temp_list: return str(num) + func(index_dict, number, temp_list[0], high+1)
            # print(low, high, num)
        
    return ''

def solution(number, k):
    number = list(number)
    
    index_dict = defaultdict(list)
    for i, v in enumerate(number): index_dict[v].append(i)
    
    return func(index_dict, number, -1, k)