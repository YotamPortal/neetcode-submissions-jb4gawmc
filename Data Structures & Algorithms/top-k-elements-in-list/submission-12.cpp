class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        for (int num: nums) {
            count[num]++;
        }
        std::vector<std::vector<int>> freqCount(nums.size() + 1);
        for (const auto& entry: count) {
            freqCount[entry.second].push_back(entry.first);
        }
        std::vector<int> res;
        for (auto rit = freqCount.rbegin(); rit != freqCount.rend(); ++rit) {
                for (int n: *rit) {
                    res.push_back(n);
                    k--;
                    if (k ==0) {
                        return res;
                    }
                }
        }
        return res;
    }
};
