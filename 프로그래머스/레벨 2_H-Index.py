# 프로그래머스_레벨 2_H-Index
# 220722

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    # v(해당 논문의 인용 수)가 i+1(해당 논문보다 인용이 많은 논문 수)보다 큰 최소 지점을 찾는 loop
    for i, v in enumerate(citations):
        if v >= (i+1): answer = i+1
        else: break
    
    
    return answer