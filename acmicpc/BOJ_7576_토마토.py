# 문제 푸는 날짜: 220322
# BOJ 7576번 토마토
# 분류: 그래프 - BFS
# 난이도: 골드 5
# https://www.acmicpc.net/problem/7576
# 문제 풀이 핵심: 순서가 중요하지 않은 목록은 list 말고 set으로 구현하자

from copy import deepcopy
import sys

def BFS():
    day_cnt = 0
    ripe_today = set()
    ripe_new = set()

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1: ripe_today.add((i, j))

    while ripe_today:
        for i, j in ripe_today:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0: ripe_new.add((nx, ny))

        for i, j in ripe_new: tomatoes[i][j] = 1
        day_cnt += 1
        ripe_today = deepcopy(ripe_new)
        ripe_new.clear()
        
    # tomatoes에 0이 있으면 -1 반환, 아니면 day_cnt - 1 값 반환
    for row in tomatoes:
        if 0 in row: return -1

    return day_cnt - 1

M, N = map(int, input().split())
tomatoes = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N): tomatoes.append([int(x) for x in sys.stdin.readline().rstrip().split()])

print(BFS())