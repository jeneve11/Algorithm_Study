# 문제 푸는 날짜: 220223
# BOJ 5555번 반지
# 분류: 문자열
# 난이도: 실버 5
# https://www.acmicpc.net/problem/5555
# 문제 풀이 핵심: 

letters = input()
count = 0
for i in range(int(input())):
    string = input()
    string += string
    if letters in string: count += 1

print(count)