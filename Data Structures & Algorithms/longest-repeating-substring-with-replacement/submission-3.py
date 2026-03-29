class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_length = 0
        count = [0] * 26
        l = r = 0
        
        while r < len(s):
            count[ord('Z') - ord(s[r])] += 1
            max_freq = max(max_freq, count[ord('Z') - ord(s[r])])
            if (r - l + 1 - max_freq) <= k:
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
               count[ord('Z') - ord(s[l])] -= 1
               l += 1
               r += 1
        return max_length 
