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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr) {
            if (subRoot != nullptr) return false;
            return true;
        }
        return sameTree(root, subRoot) || isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

    bool sameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr) {
            if (q == nullptr) return true;
            return false;
        } else if (q == nullptr) return false;

        return (p->val == q->val) && sameTree(p->left, q->left) && sameTree(p->right, q->right);
    }
};