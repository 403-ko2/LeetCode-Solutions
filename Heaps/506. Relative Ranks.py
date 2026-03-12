"""
Two solutions that follow the same intuition, first on is a solution using the sort method in python
The second solution is using heaps! A max heap storing tuples, same as the sort solution.

both have the same time complexity O(nlogn) and space complexity O(n) since both solutions are making a new array/list and use sorting n amount of times
"""

import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # arr = []

        # for index, s in enumerate(score):
        #     arr.append((s, index))
        # # print(arr)
        # arr.sort(reverse=True)
        # # print(arr)
        # res = [""] * len(score) #ex. ["", "", "", ""]

        # for i in range(len(score)):
        #     res_index = arr[i][1] #we want the tuple (1, 3) but the index which is 3

        #     if i == 0:
        #         res[res_index] = "Gold Medal"
        #     elif i == 1: 
        #         res[res_index] = "Silver Medal"
        #     elif i == 2:
        #         res[res_index] = "Bronze Medal"
        #     else:
        #         res[res_index] = str(i + 1)
            
        # return res


        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        
        res = [""] * len(score)
        place = 1
        
        while heap:
            _, idx = heapq.heappop(heap)
            
            if place == 1:
                res[idx] = "Gold Medal"
            elif place == 2:
                res[idx] = "Silver Medal"
            elif place == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(place)
            
            place += 1
        
        return res
