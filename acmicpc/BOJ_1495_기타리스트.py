# 문제 푸는 날짜: 220219
# BOJ 1495번 기타리스트
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1495
# 문제 풀이 핵심: 규칙 찾기

# 입력 받기
N, S, M = map(int, input().split())
N_list = [int(i) for i in input().split()]

dp = set({S})

for i in N_list:
    temp = set()
    for j in dp:
        if j+i <= M: temp.add(j+i)
        if j-i >= 0: temp.add(j-i)

    if not temp:
        print(-1)
        exit()

    dp = temp

# 출력
print(max(dp))