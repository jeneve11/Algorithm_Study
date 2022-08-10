# 문제 푸는 날짜: 220808
# BOJ 1927번 최소 힙
# 분류: 힙
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1927
# 문제 풀이 핵심: python에서 최대/최소값이 필요한 경우 - heapq

import heapq, sys
read = sys.stdin.readline

cnt = int(input())
max_heap = []
answer = []

for i in range(cnt):
    temp = int(read())
    # 0이 아닌 숫자일 경우 - push
    if temp: heapq.heappush(max_heap, temp)
    # 0일 경우 - pop
    elif max_heap: answer.append(heapq.heappop(max_heap))
    # 0이지만 힙이 비었을 경우 - 0 출력
    else: answer.append(0)

for i in answer: print(i)