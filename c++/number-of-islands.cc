class Solution {
public:
    void exploreIsland(vector<vector<char>>& grid, int m, int n, int x, int y) {
        stack<pair<int, int>> s;
        s.push({x, y});
        while (!s.empty()) {
            auto node = s.top();
            s.pop();

            grid[node.second][node.first] = '0';
            if (node.first + 1 < m && grid[node.second][node.first + 1] == '1') {
                s.push({node.first + 1, node.second});
            }
            if (node.first - 1 > -1 && grid[node.second][node.first - 1] == '1') {
                s.push({node.first - 1, node.second});
            }
            if (node.second + 1 < n && grid[node.second + 1][node.first] == '1') {
                s.push({node.first, node.second + 1});
            }
            if (node.second - 1 > -1 && grid[node.second - 1][node.first] == '1') {
                s.push({node.first, node.second - 1});
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid[0].size();
        int n = grid.size();

        int islandCount = 0;

        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '0') continue;
                islandCount++;
                exploreIsland(grid, m, n, j, i);
            }
        }
        return islandCount;
    }
};