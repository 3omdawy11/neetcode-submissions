class Solution {
public:
    bool isPalindrome(string s) {
        int l=0;
        int r=s.size()-1;
        while (l<r) {
            if (!isalpha(s[l]) && !isdigit(s[l])) {
                l++;
                continue;
            }
            if (!isalpha(s[r]) && !isdigit(s[l])) {
                r--;
                continue;
            }
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
        }
        return true;
    }
};