class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = {}
        for n in nums:
            hash_set[n] = 1 if n not in hash_set else hash_set[n] + 1
        seq = set()
        for num in hash_set:
            if hash_set[num] > 0 and (num-1) not in hash_set:
                seq.add(num)

        counter = 0        
        for s in seq:
            count = 1
            num = s + 1
            while num in hash_set:
                count += 1
                num += 1        
            counter = max(counter, count)
        return counter