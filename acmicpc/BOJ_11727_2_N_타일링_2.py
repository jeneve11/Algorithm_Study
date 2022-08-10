# 문제 푸는 날짜: 220810
# BOJ 11727번 2*N 타일링
# 분류: DP
# 난이도: 실버 3
# https://www.acmicpc.net/problem/11727
# 문제 풀이 핵심: 점화식 찾기

dp = [0, 1, 3]
n = int(input())
while len(dp) < n+1: dp.append((dp[-1] + 2 * dp[-2]) % 10007)
print(dp[n])