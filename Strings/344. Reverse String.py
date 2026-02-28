"""
The intuition here is to have two pointers. One starting at the beginning of the string. One at the end of the string. each iteration we swap the letter at the pointers. Once the left pointer is no longer 
less than the right pointer we know that we have successfully reversed the string. 
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        i=0
        j=n-1 
        while(i<j):
            t=s[i]
            s[i]=s[j]
            s[j]=t
            i+=1
            j-=1
