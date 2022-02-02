# 문제 푸는 날짜: 220202
# BOJ 18870번 - 좌표 압축
# 분류: ??
# 난이도: 실버2
# https://www.acmicpc.net/problem/18870
# 문제 풀이 핵심: ㅁ?ㄹ


number = int(input())
numbers_list = [int(i) for i in input().split()]

numbers_dict = {}

# 중복 제거 및 sort
new_number_list = list(set(numbers_list))
new_number_list.sort()


for i, num in enumerate(new_number_list):
    numbers_dict[num] = i

for i in numbers_list:
    print(numbers_dict[i], end= ' ')