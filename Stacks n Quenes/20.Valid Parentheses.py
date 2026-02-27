"""
utilizing a map and stack (another way would be to have several if statements to check for each bracket seperately, this way makes it simpler, but they both have similar time in complexity.)

1. create a map of the closing brackets
2. create an empty stack
3. iterate through the string
    3a. if the current iteration is in the map:
        3a.b. if the stack is not empty and the last element in the stack is equal to the map[key]: pop off the stack
        3a.c. else return False
    3b. else append the current iteration to our stack
4. return the boolean - is the stack empty or not (not stack)

O(n) time complexity (due to the for loop)
O(n) space (the map is consistant but the string itself and stack will grow as the input increases hence O(n)) 

"""

class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

#alternative solution 
"""
        stack = []

        for i in range(len(s)):
            if stack and self.pairFound(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        
        return not stack
    
    def pairFound(self, last, cur):
        return (last == "(" and cur == ")") \
                or (last == "{" and cur == "}") \
                or (last == "[" and cur == "]")
"""
