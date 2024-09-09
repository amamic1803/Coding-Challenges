#include "leetcode.hpp"

bool leetcode::Solution0009::isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    unsigned int temp_x = x;
    unsigned long long reversed_x = 0;

    while (temp_x != 0) {
        reversed_x = reversed_x * 10 + temp_x % 10;
        temp_x /= 10;
    }

    return static_cast<unsigned int>(reversed_x) == static_cast<unsigned int>(x);
}
