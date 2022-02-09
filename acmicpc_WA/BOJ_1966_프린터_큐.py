# 문제 푸는 날짜: 220209
# BOJ 1966번 프린터_큐
# 분류: ??
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1966
# 문제 풀이 핵심: ??
# 못 푼 이유: 제출 시 계속 ValueError 발생... 이유 못 찾겠다

from collections import defaultdict
import sys


def getOrder():
    printed = 0
    dict_index = defaultdict(list)
    last_so_far = 0
    length, target_index = map(int, sys.stdin.readline().rstrip().split())
    
    importance = list(map(int, sys.stdin.readline().rstrip().split()))
    target_num = importance[target_index]

    for i, v in enumerate(importance):
        dict_index[v].append(i)

    for i in range(9, target_num, -1):
        if not dict_index[i]:
            continue
        
        printed += len(dict_index[i])

        if [i for i in dict_index[i] if i < last_so_far]:
            last_so_far = max([i for i in dict_index[i] if i < last_so_far])

        else:
            last_so_far = max([i for i in dict_index[i] if i > last_so_far])

    # print(dict_index)

    if last_so_far >= target_index:
        printed += len([i for i in dict_index[target_num] if i > last_so_far or i <= target_index])
    else: # last_so_far < target_index
        printed += len([i for i in dict_index[target_num] if i > last_so_far and i <= target_index])

    return printed


num_of_case = int(input())
output_list = []

for i in range(num_of_case):
    output_list.append(getOrder())

for i in output_list:
    print(i)