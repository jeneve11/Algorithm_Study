# 문제 푸는 날짜: 220218
# BOJ 12865번 평범한 배낭
# 분류: DP
# 난이도: 골드 5
# https://www.acmicpc.net/problem/12865
# 문제 풀이 핵심: 

N, K = map(int, input().split())

pie_taste = [int(x) for x in input().split()]
cum_taste = []
cum_taste.append(sum(pie_taste[:K]))

for i in range(1, len(pie_taste)):
    if K+i <= N: cum_taste.append(cum_taste[-1] + pie_taste[K+i-1] - pie_taste[i-1])
    else: cum_taste.append(cum_taste[-1] + pie_taste[K+i-N-1] - pie_taste[i-1])

print(max(cum_taste))
