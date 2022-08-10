# 문제 푸는 날짜: 220809
# BOJ 11286번 절댓값 힙
# 분류: 힙
# 난이도: 실버 1
# https://www.acmicpc.net/problem/11286
# 문제 풀이 핵심: 2개의 힙 구현

import heapq, sys
read = sys.stdin.readline

# heap_a는 양수 입력값 보관, heap_b는 음수 입력값 보관, ans는 최종 출력값 보관
heap_a = []; heap_b = []; ans = []

N = int(input())

for i in range(N):
    a = int(read())

    # pop
    if a == 0: 
        # 둘 중 빈 힙이 있을 경우
        if not heap_a and not heap_b:
            ans.append(0)
            continue
        elif heap_a and not heap_b:
            ans.append(heapq.heappop(heap_a))
            continue
        elif not heap_a and heap_b:
            ans.append(-1 * heapq.heappop(heap_b))
            continue

        # 빈 힙이 없는 경우 비교
        temp_a = heap_a[0]
        temp_b = heap_b[0]

        # 비교하여 heap_b의 최솟값이 더 작거나 같으면, heap_b에서 pop
        if temp_a >= temp_b: ans.append(-1 * heapq.heappop(heap_b))
        # heap_a의 최솟값이 더 작으면 heap_a에서 pop
        else: ans.append(heapq.heappop(heap_a))

    # 양수 입력값일 경우 - heap_a에 push
    elif a > 0: heapq.heappush(heap_a, a)

    # 음수 입력값일 경우 - heap_b에 push
    elif a < 0: heapq.heappush(heap_b, -a)
        
# 최종 출력
for i in ans: print(i)