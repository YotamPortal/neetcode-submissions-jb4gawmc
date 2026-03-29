class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        sub_t = [0] * len(nums)
        for i in range(len(nums)):
            val = nums[i]
            if val not in nums_set:
                nums_set[val] = []
            nums_set[val].append(i)
            sub_t[i] = target - val

        for i in range(len(sub_t)):
            sub_val = sub_t[i]
            if sub_val in nums_set and i != nums_set[sub_val][0]:
                return sorted([i, nums_set[sub_val][0]])

        return [] 