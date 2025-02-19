#include "leetcode.hpp"
#include <cstddef>
#include <vector>

void leetcode::Solution0088::merge(std::vector<int>& nums1, int m, const std::vector<int>& nums2, int n) {
    std::size_t i = m + n;
    while (m != 0 && n != 0) {
        if (nums1[m - 1] >= nums2[n - 1]) {
            nums1[--i] = nums1[--m];
        } else {
            nums1[--i] = nums2[--n];
        }
    }
    while (n != 0) {
        nums1[--i] = nums2[--n];
    }
}
