class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordMap(wordList.begin(), wordList.end());
        if (wordList.empty() || beginWord ==  endWord || !wordMap.count(endWord)) {
                return 0;
        }
        if (wordMap.count(beginWord)) wordMap.erase(beginWord);

        queue<std::pair<string, int>> q;
        q.push({beginWord, 1});
        while (!q.empty()) {
                auto [word, len] = q.front();
                q.pop();
                if (word == endWord) {
                        return len;
                }
                for (char c = 'a'; c <= 'z'; c++) {
                        for (int i = 0; i < word.size(); i++) {
                                string wordTemp = word;
                                wordTemp[i] = c;
                                if (wordMap.count(wordTemp)) {
                                        q.push({wordTemp, len + 1});
                                        wordMap.erase(wordTemp);
                                }
                        }
                }        
        }
        return 0;  
    }
};
