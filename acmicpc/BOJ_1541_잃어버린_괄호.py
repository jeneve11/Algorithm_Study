# 문제 푸는 날짜: 220131
# BOJ 1541번 잃어버린 괄호
# 분류: 그리디 알고리즘
# 난이도: 실버2 
# https://www.acmicpc.net/problem/154109
# 문제 핵심: 괄호를 자유롭게 칠 수 있다 == 첫 - 이후의 모든 +를 -로 바꾸면 된다 라는 점을 파악하는 것!

input_text = input().split('-')
final_result = 0
count = 0

for i in input_text:
    nums = map(int, i.split('+'))
    sum_nums = sum(nums)
    
    if count == 0: final_result += sum_nums
    else: final_result -= sum_nums

    count += 1

print(final_result)