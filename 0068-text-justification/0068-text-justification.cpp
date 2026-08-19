class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int n = words.size();
        int i = 0;

        while (i < n) {
            int j = i;
            int totalLength = 0;

            // Find the maximum number of words for this line.
            while (j < n &&
                   totalLength + words[j].size() + (j - i) <= maxWidth) {
                totalLength += words[j].size();
                j++;
            }

            int wordCount = j - i;
            int spaces = maxWidth - totalLength;

            string line;

            // Last line or line with only one word -> left justified.
            if (j == n || wordCount == 1) {
                for (int k = i; k < j; k++) {
                    if (k > i) {
                        line += ' ';
                    }
                    line += words[k];
                }

                line += string(maxWidth - line.size(), ' ');
            }
            else {
                int gaps = wordCount - 1;
                int spacesPerGap = spaces / gaps;
                int extraSpaces = spaces % gaps;

                for (int k = i; k < j; k++) {
                    line += words[k];

                    if (k < j - 1) {
                        int gapSpaces = spacesPerGap;

                        // Left gaps receive the extra spaces.
                        if (k - i < extraSpaces) {
                            gapSpaces++;
                        }

                        line += string(gapSpaces, ' ');
                    }
                }
            }

            result.push_back(line);
            i = j;
        }

        return result;
    }
};