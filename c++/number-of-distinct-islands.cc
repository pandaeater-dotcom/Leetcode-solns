
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        int m = grid[0].size();
        int n = grid.size();
        unordered_set<string> islands;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!grid[i][j]) continue;
                string islandString = "";
                recursiveDfs(grid, islands, m, n, j, i, islandString);
                islands.insert(islandString);
            }
        }
        return islands.size();
    }

    void recursiveDfs(vector<vector<int>>& grid, unordered_set<string>& islands, int m, int n, int x, int y, string& islandString) {
        if (!grid[y][x]) return;
        grid[y][x] = 0;
        islandString += "1";
        //right
        if ((x + 1) % m != 0 && grid[y][x + 1]) {
            islandString += "r";
            recursiveDfs(grid, islands, m, n, x + 1, y, islandString);
            islandString += "b";
        }
        //left
        if (x && grid[y][x - 1]) {
            islandString += "l";
            recursiveDfs(grid, islands, m, n, x - 1, y, islandString);
            islandString += "b";
        }
        //up
        if (y && grid[y - 1][x]) {
            islandString += "u";
            recursiveDfs(grid, islands, m, n, x, y - 1, islandString);
            islandString += "b";
        }
        //down
        if (y < n - 1 && grid[y + 1][x]) {
            islandString += "d";
            recursiveDfs(grid, islands, m, n, x, y + 1, islandString);
            islandString += "b";
        }
    }
};