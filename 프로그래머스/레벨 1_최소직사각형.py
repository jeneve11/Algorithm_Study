# 프로그래머스_레벨 1_최소직사각형
# 220715

def solution(sizes):
    ans = 0
    
    # sizes 내의 모든 변수들을 nums에 저장
    nums = set()
    for a, b in sizes:
        nums.add(a)
        nums.add(b)
    
    # nums를 내림차순 list로 변환
    nums = sorted(set(nums))
    nums.reverse()
    
    # j = 최댓값
    j = nums[0]
    
    # i는 nums에서 가장 큰 요소부터 순차적으로 내려가며 진행
    for i in nums:
        for a, b in sizes:  
            if i < b and i < a:
                return j * ans
        ans = i
    
    return j * ans