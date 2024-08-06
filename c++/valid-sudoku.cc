class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> verticals(9);
        vector<unordered_set<char>> horizontals(9);
        vector<unordered_set<char>> boxes(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char square = board[i][j];
                if (square == '.') continue;
                if (!horizontals[i].insert(square).second) return false;
                if (!verticals[j].insert(square).second) return false;
                if (!boxes[3*(i/3) + (j/3)].insert(square).second) return false;
            }
        }
        return true;
    }
};
