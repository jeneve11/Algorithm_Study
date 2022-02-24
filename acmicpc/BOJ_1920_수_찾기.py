# 문제 푸는 날짜: 220223
# BOJ 1920번 수 찾기
# 분류: 자료 구조
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1920
# 문제 풀이 핵심: dictionary = hash

from collections import defaultdict

int(input())

spell_dict = defaultdict(int)
num_list = [int(x) for x in input().split()]
for num in num_list: spell_dict[num] = 1

int(input())

num_list_2 = [int(x) for x in input().split()]
for num in num_list_2: print(spell_dict[num])