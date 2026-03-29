class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for val in nums:
            counts[val] += 1

        sorted_items = dict(sorted(counts.items(), reverse=True, key=lambda item: item[1]))
        return list(sorted_items)[:k]

