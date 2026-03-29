class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(char for char in s if char.isalnum()).lower()
        length = len(clean_str)
        if length == 0:
            return True

        i = 0
        j = length - 1

        while i < j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        
        return True

        