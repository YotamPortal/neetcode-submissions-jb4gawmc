class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        l = r = 0
        uniq_set = set()
        while r < len(s):
            if s[r] not in uniq_set:
                uniq_set.add(s[r])
                # Update maxCount using current window size
                maxCount = max(maxCount, r - l + 1)
                r += 1
            else:
                # Just remove the leftmost character and move 'l'
                # The next iteration will check s[r] again
                uniq_set.remove(s[l])
                l += 1

        return maxCount 
        