class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
        count = 0
        countT = 0
        last = math.inf
        while min_heap:
            num = heapq.heappop(min_heap)
            print(num)
            if abs(num - last) <= 1 or last == math.inf:
                if num != last:
                    countT += 1
            else:
                countT = 1
            count = max(count, countT)
            last = num
        return count

        