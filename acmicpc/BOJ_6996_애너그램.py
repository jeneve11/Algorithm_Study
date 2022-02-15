# 문제 푸는 날짜: 220215
# BOJ 6996번 애너그램
# 분류: 문자열
# 난이도: 브론즈 1
# https://www.acmicpc.net/problem/6996
# 문제 풀이 핵심: EZ

from collections import defaultdict
import sys


for i in range(int(input())):
    word_dict = defaultdict(int)
    word_1, word_2 = sys.stdin.readline().rstrip().split()
    for spel in word_1:
        word_dict[spel] += 1

    for spel in word_2:
        word_dict[spel] -= 1

    if set(word_dict.values()) == {0}:
        print('{} & {} are anagrams.'.format(word_1, word_2))
    else:
        print('{} & {} are NOT anagrams.'.format(word_1, word_2))
