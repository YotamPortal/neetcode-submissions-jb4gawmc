class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x > y:
                heapq.heappush(max_heap, -(x-y))
        
        max_heap.append(0)
        return -max_heap[0]