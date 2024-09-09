#include "leetcode.hpp"
#include <algorithm>
#include <unordered_set>

std::vector<int> leetcode::Solution0001::twoSum(std::vector<int> &nums, int target) {
    std::unordered_set<int> nums_set = std::unordered_set<int>(nums.begin(), nums.end());

    for (int i = 0; i < static_cast<int>(nums.size()); i++) {
        int complement = target - nums[i];

        if (nums_set.find(complement) != nums_set.end()) {
            for (int j = 0; j < static_cast<int>(nums.size()); j++) {
                if (nums[j] == complement && i != j) {
                    return std::vector<int>{i, j};
                }
            }
        }
    }

    return std::vector<int>{};
}
