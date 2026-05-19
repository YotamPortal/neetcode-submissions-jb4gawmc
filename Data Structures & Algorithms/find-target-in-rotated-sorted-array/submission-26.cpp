class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                return mid;
            } 
            
            // Left side is sorted
            if (nums[mid] >= nums[l]) { // Pro-tip: comparing to nums[l] is safer than nums[r]
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid - 1; // Target is in the sorted left
                } else {
                    l = mid + 1;
                }
            } 
            // Right side is sorted
            else { 
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1; // Target is in the sorted right
                } else {
                    r = mid - 1; // Target is in the left
                }
            } 
        }
        return -1;    
    }
};
