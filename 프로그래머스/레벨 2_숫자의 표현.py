# 프로그래머스_레벨 2_숫자의 표현
# 220806

# 이분 탐색: 이미 정렬된 list에서 search 연산이 제일 빠름 - 시간복잡도: O(log N)
def bin_search(target, cum_sum):
    low = 0; high = len(cum_sum)-1    
    
    while high >= low:
        mid = (low + high) // 2
        
        if cum_sum[mid] == target: return 1
        
        if cum_sum[mid] > target: high = mid - 1
        else: low = mid + 1
            
    return 0
    
# 총 시간 복잡도 예상 - O(nlogn)
def solution(n):
    answer = 0
    
    # 누적합 list를 생성
    cum_sum = [i for i in range(1, n+1)]
    for i in range(n):
        if i != 0: cum_sum[i] += cum_sum[i-1]
    
    cum_sum = [0] + cum_sum
    
    # 누적합 리스트를 돌며 해당 idx의 숫자보다 n만큼 큰 idx가 있는 지 체크하여 있으면 answer += 1
    for i in cum_sum: answer += bin_search(n+i, cum_sum)
    return answer

    