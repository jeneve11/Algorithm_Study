# 문제 푸는 날짜: 220202
# BOJ 1620번 - 나는야 포켓몬 마스터 이다솜
# 분류: ??
# 난이도: 실버4 
# https://www.acmicpc.net/problem/1620
# 문제 풀이 핵심: dictionary 사용

import sys


input_nums = [int(i) for i in input().split()]

# 포켓몬 데이터 집어넣을 배열, 딕셔너리와 최종 정답 배열 생성
pokemon_list = [0] * input_nums[0]
answer_list = [0] * input_nums[1]
pokemon_dict = {}

# N개의 포켓몬 데이터 pokemon_list 배열과 pokemon_dict 딕셔너리에 입력
for i in range(input_nums[0]):
    temp_str = sys.stdin.readline().rstrip()
    pokemon_list[i] = temp_str
    pokemon_dict[temp_str] = i+1

# M개의 질문에 대한 답변 answer_list 배열에 입력
for i in range(input_nums[1]):
    input_str = sys.stdin.readline().rstrip()
    # 숫자 case
    if input_str.isdigit():
        answer_list[i] = pokemon_list[int(input_str) - 1]
    # 문자열 case
    else:
        answer_list[i] = pokemon_dict[input_str]

# answer_list 배열 출력
for i in answer_list:
    print(i)