# 문제 푸는 날짜: 220220
# BOJ 1254번 팰린드롬 만들기
# 분류: 문자열
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1254
# 문제 풀이 핵심: ??

text = list(input())

for i in range(len(text)):
    # 맨 끝 문자를 포함하는 가장 긴 팰린드롬 문자열 탐색
    if text[i:] == text[i:][::-1]:
        print(len(text) + i)
        break