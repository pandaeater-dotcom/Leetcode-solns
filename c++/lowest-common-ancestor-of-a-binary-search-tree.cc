/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (isDescendant(root->left, p) && isDescendant(root->left, q)) return lowestCommonAncestor(root->left, p, q);
        if (isDescendant(root->right, p) && isDescendant(root->right, q)) return lowestCommonAncestor(root->right, p, q);
        return root;   
    }

    bool isDescendant(TreeNode* p, TreeNode* q) {
        if (p == nullptr) return false;
        if (p->val == q->val) return true;
        return isDescendant(p->left, q) || isDescendant(p->right, q);
    }
   
};



class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int small = min(p->val, q->val);
        int large = max(p->val, q->val);

        TreeNode* node = root;
        while (large < node->val) {
            node = node->left;
        }
        while (small > node->val) {
            node = node->right;
        }
        // if (large < val) return lowestCommonAncestor(root->left, p, q);
        // if (small > val) return lowestCommonAncestor(root->right, p, q);
        return node;
    }
   
};