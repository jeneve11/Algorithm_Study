# 문제 푸는 날짜: 220306
# BOJ 2805번 나무 자르기
# 분류: 이분 탐색
# 난이도: 실버 3
# https://www.acmicpc.net/problem/2805
# 문제 풀이 핵심: 

# 입력 받기
tree_num, target = map(int, input().split())
trees = [int(x) for x in input().split()]

start = 0; end = max(trees)

# 이진 탐색
while start <= end:
    mid = (start + end) // 2

    tree_get = 0
    for tree in trees:
        if tree > mid:
            tree_get += tree - mid

    # 탈출
    if tree_get == target:
        start = mid + 1
        end = mid

    elif tree_get > target: start = mid + 1
    else: end = mid - 1

print(end)