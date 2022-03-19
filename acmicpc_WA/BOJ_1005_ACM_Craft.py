# 문제 푸는 날짜: 220317
# BOJ 1005번 ACM Craft
# 분류: DP + DFS
# 난이도: 골드 3
# https://www.acmicpc.net/problem/1005
# 문제 풀이 핵심: 

from collections import defaultdict
import sys

sys.setrecursionlimit( 10 ** 6 )


def findBuildTime(target):
    if cum_times[target]: return cum_times[target]
    if not build_rules[target]:
        cum_times[target] = build_times[target]
        return build_times[target]

    ret = 0
    for rule in build_rules[target]:
        ret = max(ret, build_times[target] + findBuildTime(rule))

    cum_times[target] = ret
    return ret

for _ in range(int(sys.stdin.readline().rstrip())):
    buildings, rules = map(int, sys.stdin.readline().rstrip().split())
    build_times = [0] + [int(x) for x in sys.stdin.readline().rstrip().split()]
    cum_times = [0] * len(build_times)
    build_rules = defaultdict(list)

    for i in range(rules):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        build_rules[b].append(a)

    print(findBuildTime(int(sys.stdin.readline().rstrip())))
    print(cum_times)