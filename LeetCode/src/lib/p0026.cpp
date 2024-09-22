#include "leetcode.hpp"

int leetcode::Solution0026::removeDuplicates(std::vector<int> &nums) {
    if (nums.empty())
        return 0;

    int unique = 1;
    for (int i = 1; i < nums.size(); i++)
        if (nums[i] != nums[unique - 1])
            nums[unique++] = nums[i];

    return unique;
}
