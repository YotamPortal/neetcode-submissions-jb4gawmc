class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> closeToOpen = { 
                                                {')' ,'('}, 
                                                {'}' ,'{'}, 
                                                {']' ,'['}
        };
        std::stack<char> _stack;
        for (char c: s) {
            if (closeToOpen.count(c)) {
                if (!_stack.empty() && _stack.top() == closeToOpen[c]) {
                    _stack.pop();
                } else {
                    return false;
                }
            } else {
                _stack.push(c);
            } 
        }
        return _stack.empty();    
    }
};
