"""
This is a premium leetcode problem, its free on lintcode and neetcode.
O(n) time complexity
the intuition is to account for the possibility that the string containing the delimiter we establish so we need another piece of data to tell us where to stop
for each word. so we combine the use of an integer signifying how long the word is and the delimiter "#". when we read over the integer and see the first instance
of our delimiter we know that we will take from the next character to where our integer spans.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res # "4#look3#ups"

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s): #while inbounds
            j = i
            while s[j] != "#":
                j += 1 #we are still looking at an integer
            length = int(s[i:j]) #this should give us just the integer we set in our encode method
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
