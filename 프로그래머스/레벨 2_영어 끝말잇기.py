# 프로그래머스_레벨 2_영어 끝말잇기
# 220814

from collections import defaultdict

def solution(n, words):
    word_dict = defaultdict(bool)
    prev = '?'
    for idx, word in enumerate(words):
        # 이미 이전에 나온 단어인지 확인
        if word_dict[word]: return [(idx % n) + 1, (idx // n) + 1]
        else: word_dict[word] = True
        
        # 이전 단어의 끝말잇기가 되는지 확인
        if prev == word[0] or prev == '?': prev = word[-1]    
        else: return [(idx % n) + 1, (idx // n) + 1]
        
    return [0, 0]