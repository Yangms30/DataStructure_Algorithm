from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
    
    def binary_search(self, nums: List[int], target: int, first: int, last: int) -> int:
        if first > last:  # 종료 조건: 탐색 범위가 유효하지 않을 때
            return -1

        mid = (first + last) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, first, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, last)