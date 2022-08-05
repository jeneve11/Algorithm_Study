# 프로그래머스_레벨 2_피로도
# 220803

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for case in list(permutations(dungeons, len(dungeons))):
        temp_k = k
        
        for i, v in enumerate(case):
            # 최소 필요 피로도보다 낮아 진행하지 못할 때
            if v[0] > temp_k:
                if answer < i: answer = i
                break

            # 최소 필요 피로도보다 높아 진행 가능할 때
            if v[0] <= temp_k:
                temp_k -= v[1]

                # 마지막까지 다 진행했다면, 던전 길이를 반환
                if i == len(dungeons)-1:
                    answer = i+1
    
    return answer