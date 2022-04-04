# 문제 푸는 날짜: 220403
# BOJ nnnn번 예시
# 분류: 
# 난이도: 실버 1
# acmicpc.net/problem/16926
# 문제 풀이 핵심: 

import sys


arr = []
N, M, R = map(int, input().split())

for _ in range(N): arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# for i in arr: print(*i)

print()

print(*arr)