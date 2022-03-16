# 문제 푸는 날짜: 220315
# BOJ 1446번 지름길
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1446
# 문제 풀이 핵심: 

from collections import defaultdict

def dpFunc(now, goal, cost):
    if now >= goal: return cost
    try: next = min([x for x in list(shortcuts_dict.keys()) if x >= now])
    except: return cost + goal - now
    cost += (next - now)
    now = next

    ret = dpFunc(now + 1, goal, cost + 1)
    for i in range(len(shortcuts_dict[now])):
        ret = min(ret, dpFunc(shortcuts_dict[now][i][0], goal, cost+shortcuts_dict[now][i][1]))

    return ret


num_shortcut, total_dist = map(int, input().split())
shortcuts_dict = defaultdict(list)

for i in range(num_shortcut):
    start, fin, dist = map(int, input().split())
    if fin > total_dist: continue
    shortcuts_dict[start].append([fin, dist])
    
print(dpFunc(0, total_dist, 0))