class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;

        string conS(s);
        conS.erase(std::remove_if(conS.begin(), conS.end(), [](unsigned char c) {
            return !std::isalnum(c);
        }), conS.end());
        int l = 0;
        int r = conS.size() - 1;
        while (l < r) {
            if (std::tolower(conS[l]) != std::tolower(conS[r])) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};
