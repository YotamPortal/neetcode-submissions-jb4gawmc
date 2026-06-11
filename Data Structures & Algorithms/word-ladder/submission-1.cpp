class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_set<string> wordSet(wordList.begin(), wordList.end());

        // אם מילת היעד לא קיימת, אין טעם להמשיך
        if (!wordSet.count(endWord)) return 0;

        std::queue<std::pair<string, int>> q;
        q.push({beginWord, 1});

        // אם מילת ההתחלה נמצאת בסט, נמחק אותה כדי שלא נחזור אליה
        if (wordSet.count(beginWord)) {
                wordSet.erase(beginWord);
        }

        while (!q.empty()) {
                auto [word, len] = q.front();
                q.pop();
                if (word == endWord) {
                        return len;
                }
                for (int c = 0; c < word.size(); c++) {
                        for (int j = 0; j < 26; j++) {
                                string tempWord = word;
                                tempWord[c] = 'a' + j;
                                if (wordSet.count(tempWord)) {
                                        wordSet.erase(tempWord);
                                        q.push({tempWord, len + 1});
                                }
                        }
                }
        }
        return 0;    
    }
};
