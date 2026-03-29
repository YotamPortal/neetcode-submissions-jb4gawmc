class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_s = {}
        for c in s:
            if c in list_s:
                list_s[c] += 1
            else:
                list_s[c] = 1
        
        list_t = {}
        for c in t:
            if c in list_t:
                list_t[c] += 1
            else:
                list_t[c] = 1

        return list_t == list_s
        
