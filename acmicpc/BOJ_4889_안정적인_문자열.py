# 문제 푸는 날짜: 220402
# BOJ 4889번 안정적인 문자열
# 분류: 그리디 알고리즘
# 난이도: 실버 1
# https://www.acmicpc.net/problem/4889
# 문제 풀이 핵심: 

import sys

output = []

while True: 
    string = sys.stdin.readline().rstrip()
    if '-' in string: break

    anal_list = []
    for i in string:
        anal_list.append(i)
        try:
            if anal_list[-2] == '{' and anal_list[-1] == '}':
                anal_list.pop(); anal_list.pop()
        except: continue
    
    cnt = 0
    while anal_list:
        if anal_list[-1] == '{': cnt += 1
        if anal_list[-2] == '}': cnt += 1
        anal_list.pop(); anal_list.pop()

    output.append(cnt)

for i, v in enumerate(output): print('{}. {}'.format(i+1, v))
