class Solution {
private:
    bool isNum(char c) {
        return ((int) c >= 48 and (int) c <= 57);
    }
public:
    string decodeString(string s) {
        int depthCounter = 0;
        vector<string> phrases;
        bool inPhrase = false;
        string curStr = "";

        for (char c : s) {
            curStr += c;
            if (c == '[') {
                depthCounter++;
                if (!inPhrase) inPhrase = true;
            }
            if (c == ']') {
                depthCounter--;
                if (depthCounter) continue;
                inPhrase = false;
                phrases.push_back(curStr);
                curStr = "";
            }
        }
        phrases.push_back(curStr);

        int repeater = 0;
        string str = "";
        string output = "";
        bool inStr = false;

        for (const auto& phrase : phrases) {
            for (int i = 0; i < phrase.size(); ++i) {
                char c = phrase[i];
                if (isNum(c)) {
                    if (!inStr) {
                        repeater = repeater * 10 + c - '0';
                        output += str;
                        str = "";
                        continue;
                    }
                    str += decodeString(phrase.substr(i, phrase.size() - i - 1));
                    cout << str;
                    i = phrase.size() - 2;
                } else if  (c == '[') {
                    inStr = true;
                } else if (c == ']') {
                    inStr = false;
                    for (int i = 0; i < repeater; ++i) {
                        output += str;
                    }
                    str = "";
                    repeater = 0;
                } else {
                    str += c;
                }
            }
        }
        output += str;

        return output;
    }
};