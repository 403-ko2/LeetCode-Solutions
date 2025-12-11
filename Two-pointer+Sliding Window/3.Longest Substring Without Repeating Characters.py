"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l, r = 0, 0
        freq = {}
        maxlen = 0

        while r < n:
            char = s[r]
            if char in freq and freq[char] >= l:
                    l = freq[char] + 1
            freq[char] = r 

            window_size = r-l+1
            if window_size > maxlen:
                maxlen = window_size
            r += 1

        return maxlen
