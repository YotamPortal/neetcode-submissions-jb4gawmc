class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[position[i], speed[i]] for i in range(len(position))]
        arr.sort(reverse=True, key=lambda x: x[0])

        stack = []
        countFleet = 0
        for i in range(len(arr)):
            timeToTarget = (target - arr[i][0]) / arr[i][1]
            while stack and stack[-1] < timeToTarget:
                stack.pop()
                if not stack:
                    countFleet += 1
            stack.append(timeToTarget)

        return countFleet + (1 if stack else 0)