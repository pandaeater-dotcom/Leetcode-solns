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
    int goodNodes(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return 1 + recursiveGoodNodes(root->left, root->val) + recursiveGoodNodes(root->right, root->val);
    }

    int recursiveGoodNodes(TreeNode* root, int largestAncestor) {
        if (root == nullptr) {
            return 0;
        }
        if (root->val < largestAncestor) {
            return recursiveGoodNodes(root->left, largestAncestor) + recursiveGoodNodes(root->right, largestAncestor);
        } else {
            return 1 + recursiveGoodNodes(root->left, root->val) + recursiveGoodNodes(root->right, root->val);
        }
    }
};