class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_set<string> wordSet;
        for (const auto& w: wordList) {
                wordSet.insert(w);
        }
        std::unordered_map<string, string> parent;
        std::queue<string> q;
        q.push(beginWord);
        while (!q.empty()) {
                string word = q.front();
                q.pop();
                if (word == endWord) {
                        int count = 0;
                        string curr = endWord;
                        while (curr != beginWord) {
                                curr = parent[curr];
                                count++;
                        }
                        return count + 1;
                }
                for (int c = 0; c < word.size(); c++) {
                        for (int j = 0; j < 26; j++) {
                                string tempWord = word;
                                tempWord[c] = 'a' + j;
                                if (wordSet.count(tempWord) && !parent.count(tempWord)) {
                                        q.push(tempWord);
                                        parent[tempWord] = word;
                                }
                        }
                }
        }
        return 0;    
    }
};
