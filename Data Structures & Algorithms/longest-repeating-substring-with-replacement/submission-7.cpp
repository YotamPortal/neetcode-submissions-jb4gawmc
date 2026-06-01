class Solution {
    public:
        int characterReplacement(string s, int k) {
                int maxFreq = 0;
                int maxRep = 0;
                int l = 0;
                std::vector<int> count(26, 0);
                for (int r = 0; r < s.size(); r++) {
                        count[s[r] - 'A']++;
                        maxFreq = std::max(maxFreq, count[s[r] - 'A']);
                        while ((r - l + 1) - maxFreq > k) {
                                count[s[l] - 'A']--;
                                l++;
                        }
                        maxRep = std::max(maxRep, r - l + 1);
                }
                return maxRep;
        }    
};
