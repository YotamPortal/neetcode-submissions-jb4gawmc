class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(char for char in s if char.isalnum()).lower()

        i = 0
        j = len(clean_str) - 1

        while i < j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        
        return True

        