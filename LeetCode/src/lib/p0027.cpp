#include "leetcode.hpp"

int leetcode::Solution0027::removeElement(std::vector<int> &nums, int val) {
    for (int i = 0; i < nums.size();) {
        if (nums[i] == val) {
            nums[i] = nums.back();
            nums.pop_back();
        } else {
            i++;
        }
    }
    return static_cast<int>(nums.size());
}
