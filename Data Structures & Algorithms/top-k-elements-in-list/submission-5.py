class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for val in nums:
            counts[val] += 1

        freq_list = [[] for _ in range(len(nums) + 1)]
        for val, freq in counts.items():
            freq_list[freq].append(val)
        
        res = []
        for arr in reversed(freq_list):
            for val in arr:
                res.append(val)
                if k == len(res):
                    return res
        return res
