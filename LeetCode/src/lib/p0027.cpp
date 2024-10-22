#include "leetcode.hpp"
#include <vector>

int leetcode::Solution0027::removeElement(std::vector<int> &nums, int val) {
    for (int i = 0; i < static_cast<int>(nums.size());) {
        if (nums[i] == val) {
            nums[i] = nums.back();
            nums.pop_back();
        } else {
            i++;
        }
    }
    return static_cast<int>(nums.size());
}
