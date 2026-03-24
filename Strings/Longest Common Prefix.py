class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        first_word = strs[0]

        for i in range(len(first_word)): #use the length so we get the index rather than the value
            for word in strs:
                if i < len(word) and first_word[i] == word[i]: #if I is less then the length of the current word and the first letter matches
                    continue
                else:  #else we return the prefix
                    return prefix
            prefix += word[i] #if each word has the letter in common the we add it to our prefix

        return prefix # return the prefix
