# 문제 푸는 날짜: 220218
# BOJ 12865번 평범한 배낭
# 분류: DP
# 난이도: 골드 5
# https://www.acmicpc.net/problem/12865
# 문제 풀이 핵심: 

import sys

num, weight = map(int, input().split())
things_weight = []
things_val = []

for _ in range(num):
    temp_weight, temp_val = map(int, sys.stdin.readline().rstrip().split())
    things_weight.append(temp_weight)
    things_val.append(temp_val)

print(things_weight)
print(things_val)