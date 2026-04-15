class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int numOfIslands = 0;
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[row].size(); col++) {
                if (grid[row][col] == '1') {
                    numOfIslands++;
                    dfs(row, col, grid);
                }
            }
        }
        return numOfIslands;        
    }

    void dfs(int row, int col, vector<vector<char>>& grid) {
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[row].size() || grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        dfs(row + 1, col, grid);
        dfs(row, col + 1, grid);
        dfs(row - 1, col, grid);
        dfs(row, col - 1, grid); 
    }
};
