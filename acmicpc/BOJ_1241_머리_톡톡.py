# 문제 푸는 날짜: 220301
# BOJ 1241번 머리 톡톡
# 분류: 수학
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1241
# 문제 풀이 핵심: 약수 구하는 알고리즘 - root(n)

import math

# number의 약수 list를 반환하는 함수
def getDiv(number):
    div_set = set()
    for i in range(1, math.ceil(number ** (1/2))):
        if number % i == 0:
            div_set.add(i)
            div_set.add(number // i)

    # 제곱수 case
    if math.ceil(number ** (1/2)) ** 2 == number:
        div_set.add(math.ceil(number ** (1/2)))

    return list(div_set)

from collections import defaultdict
import sys

nums = []
cnt_dict = defaultdict(int)

# N개 input 받아 dictionary에 입력
for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    cnt_dict[num] += 1

# 출력
for num in nums:
    temp = 0
    for i in getDiv(num): temp += cnt_dict[i]
    print(temp - 1)