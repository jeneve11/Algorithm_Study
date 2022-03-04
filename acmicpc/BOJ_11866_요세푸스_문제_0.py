# 문제 푸는 날짜: 220305
# BOJ 11866번 요세푸스 문제 0 
# 분류: 구현, 자료 구조
# 난이도: 실버 4
# https://www.acmicpc.net/problem/11866
# 문제 풀이 핵심: 

N, K = map(int, input().split())
jose_list = list(range(1, N+1))
output_list = []

now = 0
while len(output_list) < N:
    cnt = 0
    while cnt < K:
        if jose_list[now]: cnt += 1

        now += 1
        if now == N: now = 0


    jose_list[now-1] = 0
    if now: output_list.append(now)
    else: output_list.append(N)

print('<', end='')
print(*output_list, sep=', ', end='')
print('>')