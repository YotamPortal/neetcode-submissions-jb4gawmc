class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i, val in enumerate(nums):
            nums_set[val] = i

        for i, val in enumerate(nums):
            sub_val = target - val
            if sub_val in nums_set and i != nums_set[sub_val]:
                return [i, nums_set[sub_val]]

        return [] 
        