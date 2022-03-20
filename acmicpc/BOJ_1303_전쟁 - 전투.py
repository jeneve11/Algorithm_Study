# 문제 푸는 날짜: 220320
# BOJ 1303번 전쟁 - 전투
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1303
# 문제 풀이 핵심: 

from collections import deque
import sys

N, M = map(int, input().split())
warfield = []
alreadySeak = []
W_count = 0; B_count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(M):
    alreadySeak.append([False] * N)

for _ in range(M):
    warfield.append(sys.stdin.readline().rstrip())

for i in range(M):
    for j in range(N):
        if alreadySeak[i][j]: continue

        color = warfield[i][j]
        visited_right = set()
        visited_left = set()
        queue = deque()
        queue.append([i, j])

        while queue:
            now = queue.popleft()
            
            if warfield[now[0]][now[1]] == color:
                visited_right.add((now[0], now[1]))
                alreadySeak[now[0]][now[1]] = True

                for k in range(4):
                    nx = now[0] + dx[k]
                    ny = now[1] + dy[k]

                    if nx >= 0 and ny >= 0 and nx < M and ny < N and (nx, ny) not in visited_right and (nx, ny) not in visited_left:
                        queue.append([nx, ny])

            else: visited_left.add((now[0], now[1]))


        if color == 'B': B_count += (len(visited_right) ** 2)
        else: W_count += (len(visited_right) ** 2)
    
print(W_count, B_count)