#include <vector>
// binary search
// Given a sorted array and a target value, return the index of the target value in the array. If the target value is not found, return -1.
// You must write an algorithm with O(log n) runtime complexity.
// target belongs to [left,right]
// at this time, left = right is valid
class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int left = 0, right = nums.size() - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (nums[mid] == target) {
                    return mid;
                } else if (nums[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            return -1;
        }
};

