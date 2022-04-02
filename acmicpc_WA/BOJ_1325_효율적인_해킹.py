# 문제 푸는 날짜: 220401
# BOJ 1325번 효율적인 해킹
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1325
# 문제 풀이 핵심: 

from collections import defaultdict
import sys
sys.setrecursionlimit( 10 ** 6 )

def recursive(now):
    if cnt_list[now]: return cnt_list[now]

    cnt_list[now] = set([now])
    for node in belief_dict[now]: cnt_list[now] = cnt_list[now].union(recursive(node))

    return cnt_list[now]


N, M = map(int, input().split())
belief_dict = defaultdict(set)
cnt_list = [{}] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    belief_dict[b].add(a)

for i in range(1, N+1):
    if not cnt_list[i]: recursive(i)

for i in range(len(cnt_list)): cnt_list[i] = len(cnt_list[i])

max_cnt = max(cnt_list)
print(*[i for i, v in enumerate(cnt_list) if v == max_cnt])