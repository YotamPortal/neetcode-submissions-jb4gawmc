class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        count = 0
        l = r = 0
        uniq_set = set()
        while l <= r and r < len(s):
            if s[r] not in uniq_set:
                uniq_set.add(s[r])
                count += 1
                r += 1
            else:
                maxCount = max(maxCount, count)
                while s[l] != s[r]:
                    uniq_set.remove(s[l])
                    l += 1   
                l += 1
                count = r - l + 1
                r += 1

        return max(maxCount, count) 

            