# 프로그래머스_레벨 2_순위 검색
# 220811

from collections import defaultdict
from bisect import bisect_left

def similar(key1, key2):
    while key1:
        temp1, temp2 = key1 % 10, key2 % 10
        if temp1 != temp2 and temp2 != 9: return False
        else: key1 //= 10; key2 //= 10
            
    return True
            
def solution(info, query):
    answer = []
    anal = [['java', 'python', 'cpp'], ['backend', 'frontend'], ['junior', 'senior'], ['pizza', 'chicken']]
    dic = defaultdict(list)
    
    # info 처리
    for i in info:
        key = 0
        temp = i.split()
        score = int(temp.pop())
        
        for idx, val in enumerate(temp):
            key += (1 + (anal[idx]).index(val)) * (10 ** idx)
                
        dic[key].append(score)
    
    # dict 정렬
    for key in dic.keys(): dic[key].sort()
    
    # query 처리
    for i in query:
        temp = i.split(' and ')
        spl = temp[-1].split()
        temp.pop()
        score = int(spl.pop())
        temp += spl
        key = 0; num = 0
        
        for idx, val in enumerate(temp):
            if val == '-': key += 9 * (10 ** idx) 
            else: key += (1 + (anal[idx]).index(val)) * (10 ** idx) 
        
        # 이분 탐색 이용: 시간 복잡도 - O(log n)
        for dic_key in dic.keys():
            if similar(dic_key, key):
                num += len(dic[dic_key]) - bisect_left(dic[dic_key], score)
        answer.append(num)
        
    return answer