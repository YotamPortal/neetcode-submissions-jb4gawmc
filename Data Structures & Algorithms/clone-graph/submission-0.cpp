/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) {
                return nullptr;
        }
        std::unordered_map<Node*, Node*> oldToNew;
        std::queue<Node*> q;
        q.push(node);
        oldToNew[node] = new Node(node->val);

        while (!q.empty()) {
                Node* curr = q.front();
                q.pop();

                for (auto adj: curr->neighbors) {
                        if (!oldToNew.count(adj)) {
                                oldToNew[adj] = new Node(adj->val);
                                q.push(adj);
                        }
                        oldToNew[curr]->neighbors.push_back(oldToNew[adj]);
                }
        }
        return oldToNew[node];    
    }
};
