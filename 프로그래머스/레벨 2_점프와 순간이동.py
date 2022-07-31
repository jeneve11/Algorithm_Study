# 프로그래머스_레벨 2_점프와 순간이동
# 220731

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

dist_dict = defaultdict(int)
dist_dict[0] = 0; dist_dict[1] = 1

def get_dp(n):
    # 이미 메모된 경우 그대로 반환
    if dist_dict[n]: return dist_dict[n]

    # n이 짝수일 때
    if n % 2 == 0:
        dist_dict[n] = get_dp(n//2)
        return dist_dict[n]
    
    # n이 홀수일 때
    else:
        dist_dict[n] = get_dp(n//2) + 1
        return dist_dict[n]
    
def solution(n):
    return get_dp(n)