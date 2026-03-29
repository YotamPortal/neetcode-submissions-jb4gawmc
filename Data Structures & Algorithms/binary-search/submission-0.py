class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length <= 0:
            return -1

        left = 0
        right = length - 1
        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1