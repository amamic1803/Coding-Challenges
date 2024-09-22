#include "leetcode.hpp"

int leetcode::Solution0069::mySqrt(int x) {
    if (x <= 1)
        return x;

    unsigned int x0 = x / 2;

    unsigned int x1 = (x0 + x / x0) / 2;

    while (x1 < x0) {
        x0 = x1;
        x1 = (x0 + x / x0) / 2;
    }

    return static_cast<int>(x0);
}
