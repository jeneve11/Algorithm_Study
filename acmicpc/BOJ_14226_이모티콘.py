# 문제 푸는 날짜: 2203nn
# BOJ nnnn번 예시
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/nnnn
# 문제 풀이 핵심: 

from collections import deque
import sys

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

