class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix_arr = [1] * nums_len
        suffix_arr =[1] * nums_len
        res = [0] * nums_len
        for i in range(nums_len):
            if (i-1) >= 0:
                prefix_arr[i] = prefix_arr[i-1] * nums[i-1]

        for i in range(nums_len - 1, -1, -1):
            if (i+1) <= (nums_len - 1):
                suffix_arr[i] = suffix_arr[i+1] * nums[i+1]
        
        for i in range(nums_len):
            res[i] = prefix_arr[i] * suffix_arr[i]

        return res