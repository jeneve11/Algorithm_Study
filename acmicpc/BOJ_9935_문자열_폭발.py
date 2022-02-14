# 문제 푸는 날짜: 220214
# BOJ 9935번 문자열 폭발
# 분류: 문자열
# 난이도: 골드 4
# https://www.acmicpc.net/problem/9935
# 문제 풀이 핵심: 스택

sent = input()
bl = input()
list_bl = [i for i in bl]
len_bl = len(bl)

stack = []

for i in sent:
    stack += i
    if stack[-len_bl:] == list_bl:
        del stack[-len_bl:]

# 출력
if stack: print(''.join(stack))
else: print('FRULA')