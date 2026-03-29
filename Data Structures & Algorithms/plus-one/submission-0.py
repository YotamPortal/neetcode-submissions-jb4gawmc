class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in digits:
            num = (num * 10) + n
        
        num += 1
        return [int(x) for x in str(num)]