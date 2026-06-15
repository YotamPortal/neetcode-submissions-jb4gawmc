class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        queue<std::pair<int, int>> rottenQ;
        const vector<std::pair<int, int>> dir = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        int onesCount = 0;
        for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                        if (grid[r][c] == 2) {
                                rottenQ.push({r, c});
                        }
                        onesCount += (grid[r][c] == 1);
                }
        }
        int rottingTime = 0;
        while (!rottenQ.empty()) {
                int q_size = rottenQ.size();
                for (int i = 0; i < q_size; i++) {
                        auto [r, c] = rottenQ.front();
                        rottenQ.pop();
                        for (auto [dr, dc]: dir) {
                                int row = r + dr, col = c + dc;
                                if (row >= 0 && row < n && col >= 0 && col < m &&
                                grid[row][col] == 1) {
                                        grid[row][col] = 2;
                                        onesCount--;
                                        rottenQ.push({row, col});
                                }
                        }
                }
                rottingTime += (!rottenQ.empty());
        }
        return onesCount == 0 ? rottingTime : -1;
    }
};
