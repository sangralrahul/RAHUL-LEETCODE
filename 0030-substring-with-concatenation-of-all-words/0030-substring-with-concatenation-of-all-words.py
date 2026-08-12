from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        count = len(words)
        total_len = word_len * count
        n = len(s)
        if total_len > n:
            return []
        need = Counter(words)
        result = []
        for offset in range(word_len):
            left = offset
            window = Counter()
            matched = 0
            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word in need:
                    window[word] += 1
                    matched += 1
                    while window[word] > need[word]:
                        drop = s[left:left + word_len]
                        window[drop] -= 1
                        matched -= 1
                        left += word_len
                    if matched == count:
                        result.append(left)
                        drop = s[left:left + word_len]
                        window[drop] -= 1
                        matched -= 1
                        left += word_len
                else:
                    window.clear()
                    matched = 0
                    left = right + word_len
        return result