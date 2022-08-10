# 프로그래머스_레벨 2_모음사전
# 220808

def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    idx = [781, 156, 31, 6, 1]
    
    for ind, spell in enumerate(word):
        for i, v in enumerate(vowels):
            if spell == v:
                answer += (idx[ind] * i) + 1
                break
    
    
    return answer