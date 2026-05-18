class MinStack {
        std::stack<int> _stack;
        std::stack<int> minStack; 
public:
    MinStack() {}
    
    void push(int val) {
        _stack.push(val);
        int num = std::min(val, minStack.empty() ? val : minStack.top());
        minStack.push(num);
    }
    
    void pop() {
        if (!_stack.empty()) {
            _stack.pop();
            minStack.pop();
        }
    }
    
    int top() {
        return _stack.empty() ? -1 : _stack.top();
    }
    
    int getMin() {
        return minStack.empty() ? INT_MAX : minStack.top();    
    }
};
