class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {	
	std::vector<int> dp(amount + 1, INT_MAX);
	dp[0] = 0;
	
	for (int i = 1; i < dp.size(); i++) {
		for (int coin: coins) {
			if (i >= coin && dp[i - coin] != INT_MAX) {
			        dp[i] = std::min(dp[i], dp[i - coin] + 1);
			}
		}
	}
	
	return dp[amount] != INT_MAX ? dp[amount] : -1;    
    }
};
