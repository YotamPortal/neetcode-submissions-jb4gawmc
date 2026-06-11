class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_set<string> wordSet(wordList.begin(), wordList.end());

        // אם מילת היעד לא קיימת, אין טעם להמשיך
        if (!wordSet.count(endWord)) return 0;

        std::queue<std::pair<string, int>> q;
        
        // מתחילים עם אורך 1 (הכולל את beginWord)
        q.push({beginWord, 1});

        // אם מילת ההתחלה נמצאת בסט, נמחק אותה כדי שלא נחזור אליה
        if (wordSet.count(beginWord)) {
                wordSet.erase(beginWord);
        }

        while (!q.empty()) {
                auto [word, len] = q.front();
                q.pop();
                // הגענו ליעד! מחזירים את האורך הנוכחי
                if (word == endWord) {
                        return len;
                }
                for (int c = 0; c < word.size(); c++) {
                        for (int j = 0; j < 26; j++) {
                                string tempWord = word;
                                tempWord[c] = 'a' + j;
                                // אם המילה קיימת בסט (כלומר, חוקית ועדיין לא ביקרנו בה)
                                if (wordSet.count(tempWord)) {
                                        q.push({tempWord, len + 1});
                                        // מחיקה מהסט משמשת כסימון "ביקרנו כאן" (Visited)
                                        wordSet.erase(tempWord); 
                                }
                        }
                }
        }
        return 0;    
    }
};
