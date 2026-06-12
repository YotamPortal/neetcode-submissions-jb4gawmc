class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *std::max_element(piles.begin(), piles.end());
        int result = 0;
        while (left <= right) {
                int mid = left + (right - left) / 2;
                if (canFinish(piles, mid, h)) {
                        result = mid;
                        right = mid - 1;
                } else {
                        left = mid + 1;
                }
        }
        return result;    
    }

    bool canFinish(vector<int>& piles, int k, int h) {
        int res = 0;
        for (int pile: piles) {
                res += (pile + k - 1) / k;
        }
        return res <= h;
    }
};
