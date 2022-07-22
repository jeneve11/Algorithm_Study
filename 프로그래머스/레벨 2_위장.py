# 프로그래머스_레벨 2_위장
# 220720

from collections import defaultdict

def solution(clothes):
    answer = 1
    
    # defaultdict를 이용하여 부위별 의상 수를 count
    clothes_dict = defaultdict(int)
    for a, b in clothes: clothes_dict[b] += 1
        
    # 각 부위별 의상을 +1하여 모두 곱함
    # +1하는 이유는 그 부위를 안 입을 수도 있기 때문
    for i in list(clothes_dict.values()):
        answer *= (i+1)
    
    # 마지막에 -1하여 리턴하는 이유는 모든 부위를 안 입는 경우를 제거하기 위함
    return answer - 1