#include <cstdint>
#include <cstdlib>
#include "leetcode.hpp"

int leetcode::Solution0007::reverse(int x) {
    bool negative = x < 0;
    x = abs(x);

    int32_t reversed = 0;
    while (x != 0) {
        if (reversed > INT32_MAX / 10) {
            return 0;
        }
        reversed *= 10;
        if (reversed > INT32_MAX - x % 10) {
            return 0;
        }
        reversed += x % 10;
        x /= 10;
    }

    if (negative) {
        reversed = -reversed;
    }

    return reversed;
}
