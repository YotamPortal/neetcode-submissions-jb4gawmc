class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return {};
        }
        vector<vector<int>> res;
        std::sort(intervals.begin(), intervals.end(), [](auto a, auto b){ return a.at(0) < b.at(0);});
        vector<int> mergedInt = intervals[0];
        for (const auto& it: intervals) {
            if (it.at(0) <= mergedInt.at(1)) {
                mergedInt[1] = std::max(mergedInt.at(1), it.at(1));
            } else {
                res.push_back(mergedInt);
                mergedInt = it;
            }
        }
        if (!mergedInt.empty()) {
            res.push_back(mergedInt);    
        }
        return res;
    }
};
