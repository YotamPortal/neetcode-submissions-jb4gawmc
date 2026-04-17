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
        if (!root) return {};
        std::queue<TreeNode*> q;
        q.push(root);
        std::vector<std::vector<int>> res;
        while (!q.empty()) {
            int q_size = q.size();
            std::vector<int> curr_level;
            curr_level.reserve(q_size); // This prevents multiple reallocations of the vector as it grows inside the loop
            for (int i = 0; i < q_size; i++) {
                TreeNode* node = q.front();
                q.pop();
                curr_level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            res.push_back(curr_level);
        }
        return res;     
    }
};
