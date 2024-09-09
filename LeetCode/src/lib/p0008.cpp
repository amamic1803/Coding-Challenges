#include <cstdint>
#include "leetcode.hpp"

int leetcode::Solution0008::myAtoi(std::string s) {
    bool sign = true;  // true for positive, false for negative
    int32_t result = 0;

    auto string_iter = s.begin();
    while (string_iter != s.end() && *string_iter == ' ') {
        ++string_iter;
    }

    if (string_iter != s.end()) {
        if (*string_iter == '-') {
            sign = false;
            ++string_iter;
        } else if (*string_iter == '+') {
            ++string_iter;
        }
    }

    for (; string_iter != s.end(); ++string_iter) {
        char c = *string_iter;

        if (c >= '0' && c <= '9') {
            int digit = c - '0';

            if (result > INT32_MAX / 10) {
                return sign ? INT32_MAX : INT32_MIN;
            }
            result *= 10;

            if (result > INT32_MAX - digit) {
                return sign ? INT32_MAX : INT32_MIN;
            }
            result += digit;
        } else {
            break;
        }
    }

    if (!sign) {
        result = -result;
    }

    return result;
}
