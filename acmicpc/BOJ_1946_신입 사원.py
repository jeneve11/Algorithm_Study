# 문제 푸는 날짜: 220327
# BOJ 1946번 신입 사원
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1946
# 문제 풀이 핵심: 

import sys


for _ in range(int(input())):
    N = int(input())
    nums = []
    fire = set()

    for i in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        nums.append((a, b))

    min_rank = sys.maxsize
    nums.sort()

    for i, v in nums:
        if v > min_rank: fire.add((i, v))
        else: min_rank = v

    print(len(set(nums) - fire))