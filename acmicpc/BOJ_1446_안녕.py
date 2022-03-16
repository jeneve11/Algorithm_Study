# 문제 푸는 날짜: 220316
# BOJ 1535번 안녕
# 분류: DP
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1535
# 문제 풀이 핵심: 

import sys
sys.setrecursionlimit( 10 ** 6 )

def func(index, happy, hp):
    if index >= num: return happy

    ret = func(index+1, happy, hp)
    if hp > hp_loss[index]: ret = max(ret, func(index+1, happy+happiness[index], hp-hp_loss[index]))

    return ret



num = int(input())
hp_loss = [int(x) for x in input().split()]
happiness = [int(x) for x in input().split()]

print(func(0, 0, 100))