class Solution {
public:
    int rob(vector<int>& nums) {
    	if (nums.empty()) {
		return -1;
	}
	if (nums.size() == 1) {
		return nums[0];
	}
	int prev2 = nums[0];
	int prev1 = std::max(prev2, nums[1]);
	
	for (int i = 2; i < nums.size(); i++) {
		int temp = prev1;
		prev1 = std::max(prev1, nums[i] + prev2);
		prev2 = temp;
	}
	return prev1;    
    }
};
