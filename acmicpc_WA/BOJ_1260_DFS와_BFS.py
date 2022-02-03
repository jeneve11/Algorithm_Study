# 문제 푸는 날짜: 220203
# BOJ 1260번 집합
# 분류: 그래프
# 난이도: 실버 2 
# https://www.acmicpc.net/problem/1260
# 문제 풀이 핵심: DFS, BFS 구현

import sys


dots, lines, start_point = [int(i) for i in input().split()]

for _ in range(lines):
    i, v = map(int, sys.stdin.readline().rstrip().split())
    print(i, v)
