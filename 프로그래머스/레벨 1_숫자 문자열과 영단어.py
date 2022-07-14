# 프로그래머스_레벨 1_신고 결과 받기
# 220714

def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(word_list)):
        s = s.replace(word_list[i], str(i))
    return int(s)