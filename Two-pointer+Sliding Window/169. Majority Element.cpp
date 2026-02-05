/*
three solutions here. 
first one is a brute force solution utilizing an unordered hashmap (faster than an ordered) to keep track of element count
second one sorts the array since the majority should be greater than n / 2 so if you return the nums[nums.size() / 2] you would get the element that is going over the half
last one is the boyer-moore algorithm that increments the count of the result and decrements if the next iteration is not equal to the result. it will reassign result if count is going to be negative.

*/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;
        int largest = 0;
        int result = 0;

        for (int i = 0; i < nums.size(); i++){
            if (count.count(nums[i])){
                count[nums[i]]++;
            }
            else{
                count[nums[i]] = 1;
            }
            if (count[nums[i]] > largest){
                largest = count[nums[i]];
                result = nums[i];
            }
        }

        return result;

// sorting method (O(n log n) time and O(1) or O(n) space depending on the sorting algoritm)

        // sort(nums.begin(), nums.end());
        // return nums[nums.size() / 2];

//Boyer-Moore Voting Algorithm

    //     int result = 0, count = 0;

    //     for (int num : nums){
    //         if (count == 0){
    //             result = num;
    //         }
    //         if (num == result){
    //             count += 1;
    //         }else{
    //             count -= 1; 
    //         }
    //     }
    //     return result;
    // }
};
