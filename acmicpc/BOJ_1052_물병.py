# 문제 푸는 날짜: 220316
# BOJ 1052번 물병
# 분류: 그리디 알고리즘, 비트마스킹
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1052
# 문제 풀이 핵심: 

def func(num):
    temp_list = list(str(bin(num))[2:])
    temp_list.reverse()
    for i, v in enumerate(temp_list): temp_list[i] = int(v)
    return temp_list


bottles, goal = map(int, input().split())
ret = 0
bottles_list = func(bottles)

temp_num = bottles
while sum(bottles_list) > goal:
    temp = [i for i, v in enumerate(bottles_list) if v == 1]
    ret += ((2 ** temp[1]) - (2 ** temp[0]))
    temp_num += ((2 ** temp[1]) - (2 ** temp[0]))

    bottles_list = func(temp_num)

print(ret)