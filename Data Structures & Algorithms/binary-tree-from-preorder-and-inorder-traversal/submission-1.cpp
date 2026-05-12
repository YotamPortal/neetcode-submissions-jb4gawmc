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
    std::unordered_map<int, int> inorderIdxMap;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorderIdxMap[inorder[i]] = i;
        }
        return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);        
    }

    TreeNode* build(vector<int>& preorder, int preStart, int preEnd, 
                   vector<int>& inorder, int inStart, int inEnd) {
        // BASE CASE: If the range is invalid, what do we return?
        if (preStart > preEnd || inStart > inEnd) return nullptr;

        // 1. Identify the root value (Preorder always starts with the root)
        int rootVal = preorder[preStart];
        TreeNode* root = new TreeNode(rootVal);

        // 2. Find where this root is in the Inorder array
        int inRootIdx = inorderIdxMap[rootVal];

        // 3. CALCULATE: How many nodes are in the left subtree?
        // This is the distance between inStart and inRootIdx
        int leftTreeSize = inRootIdx - inStart;

        // 4. RECURSE: Build the children
        root->left = build(preorder, preStart + 1, preEnd, inorder, inStart, inRootIdx - 1);
        root->right = build(preorder, preStart + leftTreeSize + 1, preEnd, inorder, inRootIdx + 1, inEnd);

        return root;
    }
};
