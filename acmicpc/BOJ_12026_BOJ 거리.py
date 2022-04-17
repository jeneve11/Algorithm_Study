# 문제 푸는 날짜: 220417
# BOJ 12026번 BOJ 거리
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/12026
# 문제 풀이 핵심: 

import sys

goal = int(input())

energy_list = [sys.maxsize] * goal
energy_list[0] = 0

road = input()

for i, v in enumerate(energy_list):
    if v == sys.maxsize: continue

    if road[i] == 'B': next = 'O'
    elif road[i] == 'O': next = 'J'
    elif road[i] == 'J': next = 'B'

    for j in range(i+1, goal):
        if road[j] == next: energy_list[j] = min(energy_list[j], energy_list[i] + (j-i) ** 2)

print(energy_list[-1] if energy_list[-1] != sys.maxsize else -1)