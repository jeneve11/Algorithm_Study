# 문제 푸는 날짜: 220219
# BOJ 12904번 A와 B
# 분류: 그리디? 문자열?
# 난이도: 골드 5
# https://www.acmicpc.net/problem/12904
# 문제 풀이 핵심: 

S = list(input())
T = list(input())

# 역으로 변환
while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()

    else: # T[-1] == 'B':
        T.pop()
        T.reverse()

# 출력
if S == T: print(1)
else: print(0)