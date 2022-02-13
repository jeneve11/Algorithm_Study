# 문제 푸는 날짜: 220213
# BOJ 10814번 나이순 정렬
# 분류: 자료 구조
# 난이도: 실버 5
# https://www.acmicpc.net/problem/10814
# 문제 풀이 핵심: 

from collections import defaultdict
import sys


member_dict = defaultdict(list)
ages = []

for i in range(int(input())):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    if age not in ages:
        ages.append(age)

    member_dict[age].append(name)

ages.sort()

for age in ages:
    for mems in member_dict[age]:
        print(age, mems)