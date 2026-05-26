class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return vector<vector<int>>();
        }
        std::sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++) {
            const auto& currInt = intervals[i];
            auto& lastRes = res.back();
            if (lastRes[1] >= currInt[0]) {
                lastRes[1] = std::max(lastRes[1], currInt[1]);
            } else {
                res.push_back(currInt);
            }
        }
        return res;    
    }
};
