# 문제 푸는 날짜: 220305
# BOJ 1292번 쉽게 푸는 문제 
# 분류: 
# 난이도: 실버 5
# https://www.acmicpc.net/problem/1292
# 문제 풀이 핵심: 

start, fin = map(int, input().split())

num_list = []
output = 0

# 1000개 짜리 리스트 제작
for i in range(1, 46):
    for j in range(i): num_list.append(i)

# 원하는 구간의 합 구하기
for i in range(start - 1, fin):
    output += num_list[i]

# 출력
print(output)