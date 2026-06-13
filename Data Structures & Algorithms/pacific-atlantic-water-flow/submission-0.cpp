class Solution {
public:
vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
	if (heights.empty()) return {};
	std::queue<std::pair<int,int>> q_pacific;
	std::queue<std::pair<int,int>> q_atlantic;
	int n = heights.size();
	int m = heights[0].size();
	int max_dim = std::max(n, m);
	vector<vector<bool>> pacificCells(n, vector<bool>(m, false));
	vector<vector<bool>> atlanticCells(n, vector<bool>(m, false));

        // Pacific — שורה 0 (top) + עמודה 0 (left)
        for (int col = 0; col < m; col++) {
                q_pacific.push({0, col});
                pacificCells[0][col] = true;
        }
        for (int row = 0; row < n; row++) {
                q_pacific.push({row, 0});
                pacificCells[row][0] = true;
        }

        // Atlantic — שורה n-1 (bottom) + עמודה m-1 (right)
        for (int col = 0; col < m; col++) {
                q_atlantic.push({n-1, col});
                atlanticCells[n-1][col] = true;
        }
        for (int row = 0; row < n; row++) {
                q_atlantic.push({row, m-1});
                atlanticCells[row][m-1] = true;
        }

        bfs(heights, q_pacific, pacificCells);
        bfs(heights, q_atlantic, atlanticCells);
	
	vector<vector<int>> res;
	for(int row = 0; row < n; row++) {
		for (int col = 0; col < m; col++) {
			if (pacificCells[row][col] && atlanticCells[row][col]) {
				res.push_back({row, col});
			}
		}
	}
	return res;
}

void bfs(vector<vector<int>>& heights, queue<pair<int,int>>& q, vector<vector<bool>>& visited) {
    vector<pair<int,int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!q.empty()) {
        auto [row, col] = q.front(); q.pop();
        for (auto [dr, dc] : dirs) {
            int r = row+dr, c = col+dc;
            if (r>=0 && r<heights.size() && c>=0 && c<heights[0].size()
                && !visited[r][c] && heights[r][c] >= heights[row][col]) {
                visited[r][c] = true;
                q.push({r, c});
            }
        }
    }
}
};
