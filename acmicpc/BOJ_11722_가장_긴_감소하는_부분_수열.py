# 문제 푸는 날짜: 220217
# BOJ 11722번 가장 긴 감소하는 부분 수열
# 분류: DP
# 난이도: 실버 2
# https://www.acmicpc.net/problem/11722
# 문제 풀이 핵심: 규칙 찾기

import sys

len_nums = int(input())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
dp = [1] * len_nums

for i in range(1, len_nums):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))