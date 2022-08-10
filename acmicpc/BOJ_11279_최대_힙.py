# 문제 푸는 날짜: 220808
# BOJ 11279번 최대 힙
# 분류: 힙
# 난이도: 실버 2
# https://www.acmicpc.net/problem/11279
# 문제 풀이 핵심: python에서 min heap 구현하려면? (-) 기호 이용하기

import heapq, sys
read = sys.stdin.readline

cnt = int(input())
max_heap = []
answer = []

for i in range(cnt):
    temp = int(read())
    # 0이 아닌 숫자일 경우 - push
    if temp: heapq.heappush(max_heap, -temp)
    # 0일 경우 - pop
    elif max_heap: answer.append(-1 * heapq.heappop(max_heap))
    # 0이지만 힙이 비었을 경우 - 0 출력
    else: answer.append(0)

for i in answer: print(i)