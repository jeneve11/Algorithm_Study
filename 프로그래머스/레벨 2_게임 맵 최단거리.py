# 프로그래머스_레벨 2_게임 맵 최단거리
# 220729

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps):
    queue = deque([[0, 0]])
    
    while queue:
        node = queue.popleft()
        
        # 맵 우하단 방문 시 함수 종료
        if node[0] == len(maps)-1 and node[1] == len(maps[0])-1: return maps[-1][-1]
    
        # 방문되지 않았던 노드만을 queue에 추가하므로 if node not in visited: 따위의 문장은 필요없음
            
        # 인접 지점 중 갈 수 있는 노드를 queue에 추가
        for x, y in zip(dx, dy):
            # 맵 밖을 벗어나는 경우 제외하는 if문
            if 0 <= node[0]+x <= len(maps)-1 and 0 <= node[1]+y <= len(maps[0])-1:
                # 이미 방문한 노드인지를 체크하는 if문
                if maps[node[0]+x][node[1]+y] == 1 and (node[0]+x != 0 or node[1]+y != 0):
                    maps[node[0]+x][node[1]+y] = maps[node[0]][node[1]] + 1
                    queue.append([node[0]+x, node[1]+y])
    
    # 모든 맵을 다 순회했지만 map의 우하단을 방문하지 못했을 경우, -1 반환하며 함수 종료
    return -1

def solution(maps):
    return bfs(maps)