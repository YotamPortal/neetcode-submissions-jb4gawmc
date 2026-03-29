class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        countFleet = 0
        for p, s in cars:
            timeToTarget = (target - p) / s
            while stack and stack[-1] < timeToTarget:
                stack.pop()
                if not stack:
                    countFleet += 1
            stack.append(timeToTarget)


        return countFleet + (1 if stack else 0)