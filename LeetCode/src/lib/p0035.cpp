#include "leetcode.hpp"

int leetcode::Solution0035::searchInsert(const std::vector<int>& nums, const int target) {
    int low = 0;
    int high = static_cast<int>(nums.size()) - 1;

    while (low <= high) {
        const int middle = (low + high) >> 1;

        if (nums[middle] == target)
            return middle;

        if (target > nums[middle])
            low = middle + 1;
        else
            high = middle - 1;
    }
    return low;
}
