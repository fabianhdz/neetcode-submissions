class Solution {
public:
    int count(string s, char ch) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ch) {
                ++sum;
            }
        }
        return sum;
    }
    bool isAnagram(string s, string t) {
        
        std::set<char> char_set(s.begin(), s.end());

        if (s.length() != t.length()) {
            return false;
        }

        for (auto ch : char_set) {
            if (count(s, ch) != count(t, ch)) {
                return false;
            }
        }

        return true;

    }
};
