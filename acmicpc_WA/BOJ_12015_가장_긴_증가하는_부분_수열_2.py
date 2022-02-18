# 문제 푸는 날짜: 220218
# BOJ 12015번 가장 긴 증가하는 부분 수열 2
# 분류: DP
# 난이도: 골드 2
# https://www.acmicpc.net/problem/12015
# 문제 풀이 핵심: 규칙 찾기

from collections import defaultdict
import sys

len_nums = int(input())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
dp = [1] * len_nums
dp_dict = defaultdict(set)
dp_dict[1].add(nums[0])

for i in range(1, len_nums):
    keys = sorted(dp_dict.keys(), reverse=True)
    for key in keys:
        break2 = False
        for j in dp_dict[key]:
            if j < nums[i]:
                dp_dict[key+1].add(nums[i])
                break2 = True
                break
        if break2: break
            
print(max(dp_dict))