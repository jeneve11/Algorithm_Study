# 프로그래머스_레벨 2_땅따먹기
# 220730

def solution(land):
    answer = 0
    dp = land.pop()
    
    while land:
        now = land.pop()
        maxi = max(dp)
        
        for i, v in enumerate(dp):
            now[i] += maxi
            
            if maxi == dp[i]:
                sec = sorted(dp)[2]
                now[i] -= (maxi - sec)
            
        dp = now
    
    return max(dp)