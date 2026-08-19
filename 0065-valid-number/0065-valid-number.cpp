class Solution {
public:
    bool isNumber(string s) {
        int n = s.size();
        int i = 0;

        // Optional sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            i++;
        }

        bool hasDigit = false;

        // Digits before decimal point
        while (i < n && isdigit(s[i])) {
            hasDigit = true;
            i++;
        }

        // Optional decimal point and digits after it
        if (i < n && s[i] == '.') {
            i++;

            while (i < n && isdigit(s[i])) {
                hasDigit = true;
                i++;
            }
        }

        // Must have at least one digit
        if (!hasDigit) {
            return false;
        }

        // Optional exponent
        if (i < n && (s[i] == 'e' || s[i] == 'E')) {
            i++;

            // Optional exponent sign
            if (i < n && (s[i] == '+' || s[i] == '-')) {
                i++;
            }

            bool exponentDigit = false;

            while (i < n && isdigit(s[i])) {
                exponentDigit = true;
                i++;
            }

            if (!exponentDigit) {
                return false;
            }
        }

        // Entire string must be consumed
        return i == n;
    }
};