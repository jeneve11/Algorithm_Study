# 문제 푸는 날짜: 220320
# BOJ 2667번 단지번호붙이기
# 분류: DFS
# 난이도: 실버 1
# https://www.acmicpc.net/problem/2667
# 문제 풀이 핵심: 


def DFS(i, j):
    cnt_1 = set()
    queue = []
    queue.append((i, j))
    
    while queue:
        now = queue.pop()
        visited.add(now)

        if mapp[now[0]][now[1]] == '1':
            cnt_1.add((now[0], now[1]))

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    queue.append((nx, ny))

    div.append(len(cnt_1))
    return


N = int(input())

mapp = []
div = []
visited = set()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N): mapp.append(input())

for i in range(N):
    for j in range(N):
        if mapp[i][j] == '0' or (i, j) in visited:
            continue
        
        DFS(i, j)


div.sort()
print(len(div))
for i in div: print(i)