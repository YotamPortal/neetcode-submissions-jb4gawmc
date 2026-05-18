class MinStack {
    std::stack<long long> minStack;
    long long min;
public:
    MinStack() : min(LLONG_MAX) {}
    
    void push(long long val) {
        if (minStack.empty()) {
            minStack.push(0);
            min = val;
        } else {
            minStack.push(val - min);
            if (val < min) {
                min = val;
            }
        }
    }
    
    void pop() {
        if (minStack.empty()) {
            return;
        }
        long long top = minStack.top();
        minStack.pop();
        if (top < 0) {
            min = min - top;
        }
    }
    
    int top() {
        if (minStack.empty()) {
            return -1;
        }
        long long top = minStack.top();
        if (top < 0) {
            return min;
        }
        return top + min;    
    }
    
    int getMin() {
        return min;
    }
};
