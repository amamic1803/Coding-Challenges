#include "leetcode.hpp"
#include <algorithm>
#include <string>

std::string leetcode::Solution0067::addBinary(std::string a, std::string b) {
    std::string result;

    int carry = 0;
    while (!a.empty() && !b.empty()) {
        const int valA = a.back() - '0';
        const int valB = b.back() - '0';
        a.pop_back();
        b.pop_back();
        int newVal = valA + valB + carry;
        carry = newVal >> 1;
        newVal &= 1;
        result.push_back(static_cast<char>('0' + newVal));
    }
    while (!a.empty()) {
        const int valA = a.back() - '0';
        a.pop_back();
        int newVal = valA + carry;
        carry = newVal >> 1;
        newVal &= 1;
        result.push_back(static_cast<char>('0' + newVal));
    }
    while (!b.empty()) {
        const int valB = b.back() - '0';
        b.pop_back();
        int newVal = valB + carry;
        carry = newVal >> 1;
        newVal &= 1;
        result.push_back(static_cast<char>('0' + newVal));
    }
    if (carry != 0) {
        result.push_back('1');
    }

    std::reverse(result.begin(), result.end());

    return result;
}
