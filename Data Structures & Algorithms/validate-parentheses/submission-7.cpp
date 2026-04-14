class Solution {
public:
    bool isValid(string s) {
        const std::unordered_map<char, char> closeToOpen = { 
                                                {')' ,'('}, 
                                                {'}' ,'{'}, 
                                                {']' ,'['}
        };
        std::stack<char> _stack;
        for (char c: s) {
            auto itC = closeToOpen.find(c);
            if (itC != closeToOpen.end()) {
                if (!_stack.empty() && _stack.top() == itC->second) {
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
