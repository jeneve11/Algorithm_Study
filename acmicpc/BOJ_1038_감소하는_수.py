# 문제 푸는 날짜: 220224
# BOJ 1038번 감소하는 수
# 분류: 
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1038
# 문제 풀이 핵심: 

import itertools


N = int(input())
num = [10, 55, 175, 385, 637, 847, 967, 1012, 1022, 1023] # 10Cn의 누적합
leng = -1; th = -1

for i in range(len(num)):
    if N < num[i]:
        th = num[i] - N - 1
        leng = i + 1
        break

# N > 1022일때의 예외 처리
if leng == -1 and th == -1:
    print(-1)
    exit()

nums = list(range(9, -1, -1))
num_combi = list(itertools.combinations(nums, leng))

# N <= 9일때의 예외 처리
if leng == 1:
    print(nums[th])
    exit()

# 출력
for i in list(num_combi[th]): print(i, end='')