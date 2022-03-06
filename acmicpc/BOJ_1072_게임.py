# 문제 푸는 날짜: 220306
# BOJ 1072번 게임
# 분류: 이분 탐색
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1072
# 문제 풀이 핵심: 

from math import floor


X, Y = map(int, input().split())
win_rate = Y//X

print(win_rate)

if win_rate >= 99:
    print(-1)
    exit()

start = 1; end = 1000000000

# 이분 탐색
while start < end:
    mid = (start + end) // 2

    temp_win_rate = floor((Y + mid)*100/(X + mid))
    # print(mid, start, end, temp_win_rate)

    if temp_win_rate == win_rate: start = mid + 1
    else: end = mid

print(start)