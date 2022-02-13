# 문제 푸는 날짜: 220212
# BOJ 1929번 소수 구하기
# 분류: 수학
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1929
# 문제 풀이 핵심: 에라스토테네스의 체

import math

start_num, end_num = map(int, input().split())

# 0 ~ end_num까지의 index를 가지는 list 생성 후 0, 1번 인덱스는 False 처리(무조건 소수가 아님)
num_arr = [True] * (end_num + 1)
num_arr[0] = False; num_arr[1] = False

# 에라스토테네스의 체 구현
for i in range(2, 1 + math.ceil(end_num ** (1/2))):
    if num_arr[i] == False:
        continue
    
    for j in range(i*2, end_num + 1, i):
        num_arr[j] = False

# 최종 출력
for j in [i for i, v in enumerate(num_arr) if i >= start_num and v == True]:
    print(j)