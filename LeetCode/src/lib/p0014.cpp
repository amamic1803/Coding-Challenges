#include "leetcode.hpp"
#include <string>
#include <vector>

std::string leetcode::Solution0014::longestCommonPrefix(const std::vector<std::string>& strs) {
    if (strs.empty()) {
        return "";
    }

    std::string prefix;
    for (int i = 0; ; i++) {
        const char c = strs[0][i];
        if (c == '\0') {
            return prefix;
        }
        for (int j = 1; j < static_cast<int>(strs.size()); j++) {
            if (const char other_c = strs[j][i]; other_c == '\0' || other_c != c) {
                return prefix;
            }
        }
        prefix.push_back(c);
    }
}
