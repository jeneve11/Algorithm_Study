# 문제 푸는 날짜: 220407
# BOJ 9205번 맥주 마시면서 걸어가기
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/9205
# 문제 풀이 핵심: 일단 그래프 구조를 dict로 구현한 후, DFS(or BFS)로 순회하며 goal에 도달할 수 있는지 확인하기


from collections import defaultdict, deque
import sys

# 그래프 순회하며 goal 도달 여부를 반환하는 함수
def func(start_num, goal_num):
    visited = set()
    queue = deque([start_num])
    while queue:
        now = queue.popleft()
        visited.add(now)
        if now == goal_num: return True
        for node in connection_dict[now]:
            if node not in visited: queue.append(node)

    return False


for _ in range(int(sys.stdin.readline().rstrip())):
    # get input
    conv_list = []
    conv_num = int(sys.stdin.readline().rstrip())

    now_x, now_y = map(int, sys.stdin.readline().rstrip().split())
    now = (now_x, now_y)

    for i in range(conv_num):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        conv_list.append((x, y))

    goal_x, goal_y = map(int, sys.stdin.readline().rstrip().split())
    goal = (goal_x, goal_y)

    conv_list.append((now_x, now_y))
    conv_list.append((goal_x, goal_y))

    # connection_dict에 각 node들의 연결 정보를 저장
    connection_dict = defaultdict(set)
    for i in range(len(conv_list)):
        for j in range(i+1, len(conv_list)):
            if abs(conv_list[i][0] - conv_list[j][0]) + abs(conv_list[i][1] - conv_list[j][1]) <= 1000:
                connection_dict[i].add(j)
                connection_dict[j].add(i)

    # 함수 시행 후 반환값에 따라 다른 문자열 출력
    print('happy' if func(len(conv_list) - 2, len(conv_list) - 1) else 'sad')