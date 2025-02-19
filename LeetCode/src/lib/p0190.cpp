#include "leetcode.hpp"
#include <cstdint>

uint32_t leetcode::Solution0190::reverseBits(uint32_t n) {
    uint32_t new_n = 0;
    for (int i = 0; i < 32; i++) {
        new_n = (new_n << 1) | (n & 1);
        n >>= 1;
    }
    return new_n;
}
