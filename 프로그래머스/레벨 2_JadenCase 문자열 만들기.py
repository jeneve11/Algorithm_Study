# 프로그래머스_레벨 2_JadenCase 문자열 만들기
# 220728

def solution(s):
    answer = ''
    s = list(s)
    
    for i, v in enumerate (s):
        if i == 0 or s[i-1] == ' ':
            if ord(v) >= 97 and ord(v) <= 122: answer += chr(ord(v)-32)
            else: answer += v
        
        elif s[i-1] != ' ':
            if ord(v) >= 65 and ord(v) <= 90: answer += chr(ord(v)+32)
            else: answer += v
    
    return answer