#include "leetcode.hpp"
#include <vector>

int leetcode::Solution0026::removeDuplicates(std::vector<int> &nums) {
    if (nums.empty())
        return 0;

    int unique = 1;
    for (int i = 1; i < static_cast<int>(nums.size()); i++)
        if (nums[i] != nums[unique - 1])
            nums[unique++] = nums[i];

    return unique;
}
