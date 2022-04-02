# 문제 푸는 날짜: 220329
# BOJ 14226번 이모티콘
# 분류: DP + BFS
# 난이도: 골드 5
# https://www.acmicpc.net/problem/14226
# 문제 풀이 핵심: 

from collections import deque

S = int(input())
dp = []

for i in range(1100): dp.append([0]*(S+1))

queue = deque()
queue.append((1, 1, 1))

while queue:
    node_x, node_y, sec = queue.popleft()
    try:
        if dp[node_x][node_y]: continue
        else: dp[node_x][node_y] = sec
    except: continue

    if node_x == S:
        print(sec)
        exit(0)

    # backspace
    queue.append((node_x - 1, node_y, sec + 1))
    
    # copy
    queue.append((node_x, node_x, sec + 1))

    # paste
    queue.append((node_x + node_y, node_y, sec + 1))

