class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size()-1;
        int maxArea = 0;

        while (l < r){
            int distance = r - l;
            int area = std::min(height[l],height[r]) * distance;
            maxArea = std::max(area, maxArea);
            cout << area << " " << maxArea << endl;
            if (height[l] < height[r]){
                l++;
            }else{
                r--;
            }
 
        }        
        return maxArea;
