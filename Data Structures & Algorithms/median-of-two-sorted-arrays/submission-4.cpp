class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;
        bool isEven = (n + m) % 2 == 0;

        while (low <= high) {
            int i = (high + low) / 2;
            int j = (m + n + 1) / 2 - i;
            int maxLeftA = (i == 0) ? INT_MIN : nums1[i - 1];
            int minRightA = (i == m) ? INT_MAX : nums1[i];

            int maxLeftB = (j == 0) ? INT_MIN : nums2[j - 1];
            int minRightB = (j == n) ? INT_MAX : nums2[j];

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                return isEven ? (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0 : max(maxLeftA, maxLeftB);
            } else if (maxLeftA > minRightB) {
                high = i - 1;
            } else {
                low = i + 1;
            }  
        }
        return -1;
    }
};
