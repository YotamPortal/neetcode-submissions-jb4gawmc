class Solution {
public:
    bool isValid(string s) {
        const std::unordered_map<char, char> parenthresesMap = { 
                                                {')' ,'('}, 
                                                {'}' ,'{'}, 
                                                {']' ,'['}
        };
        std::stack<char> _stack;
        for (char c: s) {
            auto itC = parenthresesMap.find(c);
            if (itC != parenthresesMap.end()) {
                if (_stack.empty()) {
                    return false;
                }
                char val = _stack.top();
                _stack.pop();
                if (val != itC->second) {
                    return false;
                }
            } else {
                _stack.push(c);
            } 
        }
        return _stack.empty();    
    }
};
