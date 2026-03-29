class Solution:
    def isHappy(self, n: int) -> bool:
        def sumThePower(num):
            return sum(int(d)**2 for d in str(abs(num)))

        seen = set() 
        while n != 1:
            n = sumThePower(n)
            if n in seen:
                return False
            seen.add(n)
        
        return True
