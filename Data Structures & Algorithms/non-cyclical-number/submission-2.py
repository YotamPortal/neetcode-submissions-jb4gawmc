class Solution:
    def isHappy(self, n: int) -> bool:
        def sumThePower(num):
            return sum(int(d)**2 for d in str(abs(num)))

        slow = n
        fast = sumThePower(n)
        while fast != slow:
            slow = sumThePower(slow)
            fast = sumThePower(sumThePower(fast))

        return fast == 1
