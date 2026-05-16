class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int missingNum = target - nums[i];
            if (map.contains(missingNum)) {
                return {map[missingNum], i};
            }
            map[nums[i]] = i;
        }
        return {};    
    }
};
