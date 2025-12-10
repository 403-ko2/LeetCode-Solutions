"""
Link: https://leetcode.com/problems/min-stack/

we want the methods to work in constant time (O(1))
stack is based on the idea of LIFO (last in first out)
"""

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        min_value = val
        if len(self.stack) > 0:
            min_value = min(self.stack[-1][1], min_value)
        
        self.stack.append([val, min_value])

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
