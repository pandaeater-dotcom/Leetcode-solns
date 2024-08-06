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
    int maxDiameter = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return 0;
        diameter(root);
        return maxDiameter;
    }
    int diameter(TreeNode* root) {
        if (root == nullptr) return 0;
        auto left = diameter(root->left);
        auto right = diameter(root->right);
        maxDiameter = max(maxDiameter, left + right);
        return 1 + max(left, right);
    }
};