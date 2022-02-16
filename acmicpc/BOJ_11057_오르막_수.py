# 문제 푸는 날짜: 220216
# BOJ 11057번 오르막 수
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/11057
# 문제 풀이 핵심: 규칙 찾기

from collections import deque


num = int(input())
dp = [0, 10, 55]
temp = deque(range(10, 0, -1))

for j in range(3, num + 1):
    for i in range(len(temp)):
        if i == 0: continue
        temp[i] += temp[i-1]

    temp.pop()
    temp.appendleft(0)

    for i in range(len(temp)):
        temp[i] = dp[-1] - temp[i]

    dp.append(sum(temp))

print(dp[num] % 10007)