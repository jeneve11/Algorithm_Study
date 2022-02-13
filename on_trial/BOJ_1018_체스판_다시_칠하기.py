# 문제 푸는 날짜: 220210
# BOJ 1018번 체스판 다시 칠하기
# 분류: 브루트 포스
# 난이도: 실버 5
# https://www.acmicpc.net/problem/1018
# 문제 풀이 핵심: 


import sys


n, m = map(int, input().split())
chess_board = []


start_w = ['WB' * (m // 2) , 'BW' * (m // 2)]

if m % 2:
    start_w[0] += 'W'
    start_w[1] += 'B'

for _ in range(n):
    chess_board.append(sys.stdin.readline().rstrip())



print(start_w)

print(chess_board)