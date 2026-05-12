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
    // We pass both a low and high constraint
    bool isValidBST_DFS(TreeNode* root, long long minVal, long long maxVal) {
        // Base case: An empty tree is valid
        if (!root) {
            return true;
        }

        // 1. Check if the current node violates the range
        if (root->val <= minVal || root->val >= maxVal) {
            return false;
        }

        // 2. Recurse Left: 
        // The current value becomes the new UPPER bound (maxVal).
        // 3. Recurse Right: 
        // The current value becomes the new LOWER bound (minVal).
        return isValidBST_DFS(root->left, minVal, root->val) && 
               isValidBST_DFS(root->right, root->val, maxVal);
    }

    bool isValidBST(TreeNode* root) {
        // We start with the largest possible range
        return isValidBST_DFS(root, LLONG_MIN, LLONG_MAX);
    }
};
