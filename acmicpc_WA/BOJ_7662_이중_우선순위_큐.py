# 문제 푸는 날짜: 220214
# BOJ 7662번 이중 우선순위 큐
# 분류: 자료 구조
# 난이도: 골드 5
# https://www.acmicpc.net/problem/7662
# 문제 풀이 핵심: 힙(heap)

import sys, heapq


for _ in range(int(input())):
    num_of_order = int(sys.stdin.readline().rstrip())
    # min_heap 초기화
    min_heap = []
    for i in range(num_of_order):
        order, num = sys.stdin.readline().rstrip().split()
        if order == 'I':
            heapq.heappush(min_heap, int(num))
        elif min_heap and num == '-1':
            if min_heap:
                heapq.heappop(min_heap)
        elif min_heap and num == '1': 
            # 최댓값 pop
            if min_heap:
                min_heap.pop(min_heap.index(heapq.nlargest(1, min_heap)[0]))

    if min_heap:
        print(heapq.nlargest(1, min_heap)[0], min_heap[0])
    else:
        print('EMPTY')