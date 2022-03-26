# 문제 푸는 날짜: 220326
# BOJ 1012번 유기농 배추
# 분류: 그래프
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1012
# 문제 풀이 핵심: 

from collections import deque


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(int(input())):
    M, N, K = map(int, input().split())

    field = []

    for i in range(M): field.append([0] * N)


    for i in range(K):
        a, b = map(int, input().split())
        field[a][b] = 1

    cnt = 0
    visited = set()

    for i in range(M):
        for j in range(N):
            if (i, j) in visited: continue

            visited.add((i, j))
            if field[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                while queue:
                    a, b = queue.popleft()
                    for k in range(4):
                        nx = a + dx[k]
                        ny = b + dy[k]

                        if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1 and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))

                cnt += 1

    print(cnt)