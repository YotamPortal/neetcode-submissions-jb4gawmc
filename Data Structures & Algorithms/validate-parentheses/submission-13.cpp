class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> closeToOpen = {
            {')' , '('},
            {'}' , '{'},
            {']' , '['}
        };
        std::stack<char> stackOpen;
        for (char c: s) {
            if (closeToOpen.find(c) != closeToOpen.end()) {
                if (!stackOpen.empty() && closeToOpen[c] == stackOpen.top()) {
                    stackOpen.pop();
                } else {
                    return false;
                }
            } else {
                stackOpen.push(c);
            }
        }
        return stackOpen.empty();    
    }
};
