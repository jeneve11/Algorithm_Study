# 문제 푸는 날짜: 220224
# BOJ 1074번 Z
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1074
# 문제 풀이 핵심: 재귀

import sys
sys.setrecursionlimit(10 ** 6)

def findPosition(N, R, C):
    cum_sum = 0
    
    # 탈출 조건
    if N == 0: return 0

    if R >= (2 ** N) / 2:
        cum_sum += (2 ** N) * (2 ** N) / 2
        R -= (2 ** N) / 2

    if C >= (2 ** N) / 2:
        cum_sum += (2 ** N) * (2 ** N) / 4
        C -= (2 ** N) / 2

    return cum_sum + findPosition(N - 1, R, C)

N, row, column = map(int, input().split())

print(int(findPosition(N, row, column)))