class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        if (strs.empty()) {
            return res;
        }
        std::unordered_map<string, vector<string>> map;
        for (const auto& str: strs) {
            int count[26] = {0};
            for (char c: str) {
                count[c - 'a']++;
            }
            string key = "";
            for (int i = 0; i < 26; i++) {
                key += std::to_string(count[i]) + "#";
            }
            map[key].push_back(str);
        }
        for (const auto& list: map) {
            res.push_back(list.second);
        }
        return res;
    }
};
