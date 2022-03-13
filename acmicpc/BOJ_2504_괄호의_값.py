# 문제 푸는 날짜: 220313
# BOJ 2504번 괄호의 값
# 분류: 
# 난이도: 실버 2
# https://www.acmicpc.net/problem/2504
# 문제 풀이 핵심: 

from collections import defaultdict
import sys

sys.setrecursionlimit( 10 ** 6 )

def anal_str(string):
    if string == '()': return 2
    elif string == '[]': return 3

    # 분석
    ret = 0; part_list = [0]
    for i, v in enumerate(string):
        if v == '(': brace_dict[2] += 1
        elif v == ')': brace_dict[2] -= 1
        elif v == '[': brace_dict[3] += 1
        elif v == ']': brace_dict[3] -= 1

        if set(brace_dict.values()) == {0}: part_list.append(i+1)

    # 올바르지 않은 문자열일 경우 - 0 출력하고 프로그램 종료
    if set(brace_dict.values()) != {0}:
        print(0)
        exit()

    # 2개 이상의 덩어리로 구성된 경우
    if len(part_list) > 2:
        for i in range(len(part_list) - 1):
            ret += anal_str(string[part_list[i]:part_list[i+1]])
    
        return ret

    # 1개 덩어리 경우 1
    elif string[0] == '(' and string[-1] == ')':
        return 2 * anal_str(string[1:-1])

    # 1개 덩어리 경우 2
    elif string[0] == '[' and string[-1] == ']':
        return 3 * anal_str(string[1:-1])

    else:
        print(0)
        exit()




brace_dict = defaultdict(int)
str_input = input()

print(anal_str(str_input))