class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freqMap;
        for (int i = 0; i < nums.size(); i++) {
            freqMap[nums[i]]++;
        }
        std::vector<std::vector<int>> freqBucket(nums.size() + 1);    
        for (const auto& freq: freqMap) {
            freqBucket[freq.second].push_back(freq.first);
        }
        std::vector<int> res;
        for (auto rit = freqBucket.rbegin(); rit != freqBucket.rend(); rit++) {
            for (auto n: *rit) {
                res.push_back(n);
                k--;
                if (k == 0) {
                    return res;
                }
            }
        }
        return res;
    }
};
