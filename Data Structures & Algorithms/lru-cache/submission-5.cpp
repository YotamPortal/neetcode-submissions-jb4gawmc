struct ListNode {
    int key = 0;
    int val = 0;
    ListNode* next = nullptr;
    ListNode* prev = nullptr;

    ListNode(int _key, int _val, ListNode* _next = nullptr, ListNode* _prev = nullptr) :
        key(_key), val(_val), next(_next), prev(_prev) {}
};

class LRUCache {
    int cap;
    std::unordered_map<int, ListNode*> keyToNode;
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new ListNode(-1,-1);
        tail = new ListNode(-1,-1);
        head->next = tail;
        tail->prev = head;    
    }

    void insert(int key, int value) {
        ListNode* newNode = new ListNode(key, value);
        keyToNode[key] = newNode;
        moveToHead(newNode);
    }

    void remove(ListNode* node) {
        if (node) {
            node->prev->next = node->next;
            node->next->prev = node->prev;
            keyToNode.erase(node->key);
            delete node;
        }
    }

    void moveToHead(ListNode* node) {
        if (node) {
            if (node->prev) {
                node->prev->next = node->next;
            }
            if (node->next) {
                node->next->prev = node->prev;
            }
            node->next = head->next;
            node->prev = head;
            head->next->prev = node;
            head->next = node;
        }
    }
    
    int get(int key) {
        int res = -1;
        if (keyToNode.count(key)) {
            res = keyToNode[key]->val;
            moveToHead(keyToNode[key]);
        }
        return res;
    }
    
    void put(int key, int value) {
        if (keyToNode.count(key)) {
            keyToNode[key]->val = value;
            moveToHead(keyToNode[key]);    
        } else {
            insert(key, value);
        }
        if (keyToNode.size() > cap) {
            remove(tail->prev);
        }     
    }
};
