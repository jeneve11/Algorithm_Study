# 문제 푸는 날짜: 220220
# BOJ 1149번 RGB거리
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1149
# 문제 풀이 핵심: 발상

import sys

# 입력
costs = []
num = int(input())
for _ in range(num): costs.append([int(i) for i in sys.stdin.readline().rstrip().split()])
    
# 각 집들을 지나며 방금 칠한 집 색깔별로(RGB) 최소비용을 메모
smallest_cost = [0] * 3
for cost in costs:
    temp = []
    temp.append(min(smallest_cost[1] + cost[0], smallest_cost[2] + cost[0]))
    temp.append(min(smallest_cost[0] + cost[1], smallest_cost[2] + cost[1]))
    temp.append(min(smallest_cost[0] + cost[2], smallest_cost[1] + cost[2]))
    smallest_cost = temp

# 출력
print(min(smallest_cost))