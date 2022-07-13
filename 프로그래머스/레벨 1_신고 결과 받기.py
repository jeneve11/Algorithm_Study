# 프로그래머스_레벨 1_신고 결과 받기
# 220713

from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ans = []
    b_dict = defaultdict(list)
    
    for i in report:
        a, b = i.split()
        if a not in b_dict[b]: b_dict[b].append(a)
    
    for i in b_dict:
        if len(b_dict[i]) >= k:
            
            for j in b_dict[i]:
                ans.append(j)
    
    for i in ans:
        for j in range(len(id_list)):
            if i == id_list[j]:
                answer[j] += 1
                
    return answer