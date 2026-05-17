class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> map;
        for(const auto& n: nums) {
            map[n]++;
        }
        std::vector<std::pair<int, int>> vec;
        for (const auto& e: map) {
            vec.push_back(std::make_pair(e.first, e.second));
        }

        // Save the lambda to a variable
        auto comp = [](const auto& a, const auto& b) {
            return a.second < b.second;
        };

        std::make_heap(vec.begin(), vec.end(), comp);
        std::vector<int> res;
        while (k) {
            res.push_back(vec.front().first);
            std::pop_heap(vec.begin(), vec.end(), comp);
            vec.pop_back();
            k--;
        }
        return res;   
    }
};
