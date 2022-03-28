# 문제 푸는 날짜: 220329
# BOJ 1543번 문서 검색
# 분류: 그리디 알고리즘
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1543
# 문제 풀이 핵심: 

doc = input()
word = input()
cnt = 0
i = 0

while True:
    if i >= len(doc): break

    if doc[i:i+len(word)] == word:
        i += len(word)
        cnt += 1
        continue

    i += 1

print(cnt)