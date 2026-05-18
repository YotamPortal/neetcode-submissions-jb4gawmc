class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        int maxLen = 0;
        int l = 0;
        int r = 0;
        std::unordered_map<char, int> count;

        while (l <= r && r < size) {
            if (!count.contains(s[r])) {
                count[s[r]] = r;
                maxLen = std::max(maxLen, r - l + 1);
                r++;
            } else {
                count.erase(s[l]);
                l++;
            }
        }

        return maxLen;    
    }
};
