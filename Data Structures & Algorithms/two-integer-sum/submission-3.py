class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i in range(len(nums)):
            nums_set[nums[i]] = i

        for i in range(len(nums)):
            sub_val = target - nums[i]
            if sub_val in nums_set and i != nums_set[sub_val]:
                return [i, nums_set[sub_val]]

        return [] 
        