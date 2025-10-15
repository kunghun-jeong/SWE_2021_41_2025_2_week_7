from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    O(n^2) 직관적 풀이: i를 고정하고 j=i+1.. 탐색.
    '처음 발견되는 (i, j)'를 즉시 반환한다.
    """
    n = len(nums)
    for i in range(n):
        need = target - nums[i]
        for j in range(i + 1, n):
            if nums[j] == need:
                return [i, j]
    # 과제는 해가 존재한다고 가정하지만, 방어적으로 빈 리스트 반환
    return []
