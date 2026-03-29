class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)

        count2 = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in count1:
                count2[s2[r]] = 1 + count2.get(s2[r], 0)
                winSize = r - l + 1
                if winSize > len(s1):
                   count2[s2[l]] = count2.get(s2[l], 0) - 1
                   l += 1
                   if count1 == count2:
                        return True
            else:
                if count1 == count2:
                    return True
                count2.clear()
                while l != r:
                    l += 1
                l += 1
        return count1 == count2  