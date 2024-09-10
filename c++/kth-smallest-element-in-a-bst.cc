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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> smallest;
        recursiveKthSmallest(root, k, smallest);
        return smallest[k - 1];
    }

    void recursiveKthSmallest(TreeNode* root, int k, vector<int>& smallest) {
        if (!k || root == nullptr) return;
        if (root->left == nullptr) {
            smallest.push_back(root->val);
            k--;
        } else {
            recursiveKthSmallest(root->left, k, smallest);
            if (k) {
                smallest.push_back(root->val);
                k--;
            }
        }
        recursiveKthSmallest(root->right, k, smallest);
    }
};