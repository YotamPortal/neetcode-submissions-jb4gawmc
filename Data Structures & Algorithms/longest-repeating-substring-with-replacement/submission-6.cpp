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
            int window = r - l + 1;
            if (window - maxFreq <= k) {
                maxRep = std::max(maxRep, window);
            } else {
                count[s[l] - 'A']--;
                l++;
            }
        }
        return maxRep;    
    }
};
