# 문제 푸는 날짜: 220323
# BOJ 4179번 불!
# 분류: BFS
# 난이도: 골드 4
# https://www.acmicpc.net/problem/4179
# 문제 풀이 핵심: 

from copy import deepcopy
import sys

def BFS(loc_j, cnt, maze):
    if loc_j[0] == 0 or loc_j[0] == R - 1 or loc_j[1] == 0 or loc_j[1] == C - 1:
        return cnt + 1

    for i in range(4):
        nx = loc_j[0] + dx[i]
        ny = loc_j[1] + dy[i]

        if maze[nx][ny] == '.': break

    else: return sys.maxsize

    visited = set()

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#':
                        visited.add((nx, ny))

    for i, j in visited: maze[i][j] = 'F'

    jx = loc_j[0]
    jy = loc_j[1]
    ret = sys.maxsize

    for i in range(4):
        nx = jx + dx[i]
        ny = jy + dy[i]

        if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.':
            temp = deepcopy(maze)
            ret = min(ret, BFS([nx, ny], cnt + 1, temp))

    return ret

maze = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
R, C = map(int, input().split())


for _ in range(R): maze.append(list(sys.stdin.readline().rstrip()))

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            maze[i][j] = '.'
            ef = BFS([i, j], 0, maze)
            if ef == sys.maxsize: print('IMPOSSIBLE')
            else: print(ef)
            exit(0)