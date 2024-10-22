#include "leetcode.hpp"
#include <vector>

int leetcode::Solution0033::search(std::vector<int> &nums, int target) {
    if (nums.empty()) {
        // no numbers, no target present
        return -1;
    }
    if (nums.size() == 1) {
        return nums[0] == target ? 0 : -1;
    }
    if (nums[0] < nums[nums.size() - 1]) {
        // not rotated, simple binary search
        int start = 0;
        int end = static_cast<int>(nums.size()) - 1;

        while (start <= end) {
            const int mid = (start + end) / 2;
            if (target < nums[mid]) {
                end = mid - 1;
            } else if (target > nums[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
    }

    // rotated, binary search to find rotation point + binary search to find target

    int rotation_point = 0;
    if (nums[0] > nums[1]) {
        rotation_point = 1;
    } else {
        int start = 1;
        int end = static_cast<int>(nums.size()) - 1;

        while (start < end - 1) {
            const int mid = (start + end) / 2;
            if (nums[mid - 1] > nums[mid]) {
                rotation_point = mid;
                break;
            }
            if (nums[start] > nums[mid]) {
                end = mid;
            } else if (nums[mid] > nums[end]) {
                start = mid;
            }
        }
        if (start == end - 1) {
            rotation_point = nums[start - 1] > nums[start] ? start : end;
        } else if (start == end) {
            rotation_point = start;
        }
    }

    const int len = static_cast<int>(nums.size());
    int start = rotation_point;
    int end = start + len - 1;

    while (start <= end) {
        const int mid = (start + end) / 2;
        if (target < nums[mid % len]) {
            end = mid - 1;
        } else if (target > nums[mid % len]) {
            start = mid + 1;
        } else {
            return mid % len;
        }
    }

    return -1;
}
