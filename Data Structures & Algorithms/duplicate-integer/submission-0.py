class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_list = {}
        for x in nums:
            if x in hash_list:
                hash_list[x] += 1
            else:
                hash_list[x] = 1

        for key in hash_list:
            if hash_list[key] > 1:
                return True

        return False
        