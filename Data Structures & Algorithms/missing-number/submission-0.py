class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fullSum = 0
        currSum = 0
        for i in range(0, len(nums) + 1):
            fullSum += i
            if i < len(nums):
                currSum += nums[i]
        
        return fullSum - currSum