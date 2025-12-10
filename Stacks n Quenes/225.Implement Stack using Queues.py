"""
Link: https://leetcode.com/problems/implement-stack-using-queues/description/

use 2 quenes(dont really need the second one)

1a. O(1) appending the element x to the "top" of the stack
2a. O(1) quenes have a pop() method that imitates the standard array method
3a. O(1) returning the last elemnt in our stack by passing in the the last index
4a. check the array if it is empty. if it is return true else return false 

if you would like to utilize both deques the solution would require flipping the elements so the back of the stack is the front of the quene using a while loop while the quene has > 1 element.
you would then be left with one element which you would store with a popleft() and return that value where needed. you would then reassign the first stack (which is not empty) to the second stack
which was appending all the elements of the first

"""
from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()
        self.ext = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
       return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
