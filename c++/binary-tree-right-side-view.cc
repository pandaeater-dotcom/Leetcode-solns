/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        recursiveRightSideView(root, 0, result);

        return result;
    }

    void recursiveRightSideView(TreeNode* root, int level, vector<int>& result) {
        if (root == nullptr) {
            return;
        }
        if (result.size() < level + 1) {
            result.push_back(root->val);
        }
        recursiveRightSideView(root->right, level + 1, result);
        recursiveRightSideView(root->left, level + 1, result);
    }
};