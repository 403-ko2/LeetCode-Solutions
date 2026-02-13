"""
Since the problem describes that the center is connected to ever node and no other nodes are connected to each other. We know that the only number that would be repeated in the 
input must be the center. Thus we only need to check the first two inputs in the array. When we find the number that repeats we return that number!

"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        map = {}

        for node1, node2 in edges:
            print(node1, node2)
            if node1 in map:
                return node1
            if node2 in map:
                return node2
            map[node1] = 1
            map[node2] = 1
