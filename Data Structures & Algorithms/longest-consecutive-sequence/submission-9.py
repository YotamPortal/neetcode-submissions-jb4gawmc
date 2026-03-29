class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = {}
        for n in nums:
            hash_set[n] = 1 if n not in hash_set else hash_set[n] + 1
        counter = 0
        for num in hash_set:
            if hash_set[num] > 0 and (num-1) not in hash_set:
                strike = 1
                val = num + 1
                while val in hash_set:     
                    val += 1
                    strike += 1
                counter = max(counter, strike)
        return counter    