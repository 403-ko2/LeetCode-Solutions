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
