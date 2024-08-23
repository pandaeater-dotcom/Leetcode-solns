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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<vector<int>> list= {{root->val}};
        recursiveLevelOrder(root->left, 1, list);
        recursiveLevelOrder(root->right, 1, list);
        return list;
    }

    void recursiveLevelOrder(TreeNode* root, int level, vector<vector<int>>& list) {
        if (root == nullptr) {
            return;
        }
        if (list.size() - 1 >= level) {
            list[level].push_back(root->val);
        } else {
            list.push_back({root->val});
        }
        recursiveLevelOrder(root->left, level + 1, list);
        recursiveLevelOrder(root->right, level + 1, list);
    }
};