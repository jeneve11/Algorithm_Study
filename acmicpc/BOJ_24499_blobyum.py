# 문제 푸는 날짜: 220221
# BOJ 24499번 blobyum
# 분류: 슬라이딩 윈도우
# 난이도: 실버 4
# https://www.acmicpc.net/problem/24499
# 문제 풀이 핵심: 

N = int(input())

tower_height = [int(x) for x in input().split()]
total_height = []

if N == 1 or N == 2:
    print(max(tower_height))
    exit()

for i in range(1, len(tower_height) - 1):
    total_height.append(tower_height[i] + min(tower_height[i-1], tower_height[i+1]))

print(max(max(total_height), tower_height[0], tower_height[-1]))